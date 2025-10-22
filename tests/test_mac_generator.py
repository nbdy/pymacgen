import re
import unittest
import sys
import types

# pymacgen is imported later after injecting a fake 'pyoui' and 'loguru' modules


class FakeOuiEntry:
    def __init__(self, prefix: str):
        self.prefix = prefix


class FakeOUIParsed:
    def __init__(self):
        # lowercase keys to allow case-insensitive lookups
        self._org = {
            "apple": [FakeOuiEntry("AA:BB:CC")],
            "samsung": [FakeOuiEntry("12:34:56")],
            "nokia": [FakeOuiEntry("00:11:22")],
        }
        self._by_country_name = {
            "germany": [FakeOuiEntry("DE:AD:BE")],
            "united states": [FakeOuiEntry("FE:ED:FA")],
        }
        self._by_country_code = {
            "DE": [FakeOuiEntry("DE:00:00")],
            "US": [FakeOuiEntry("FA:CE:00")],
        }

    # In real lib these are likely generators; returning a list is fine for tests
    def by_organization(self, name):
        return self._org.get(str(name).lower(), [])

    def by_country_name(self, name):
        return self._by_country_name.get(str(name).lower(), [])

    def by_country_code(self, code):
        return self._by_country_code.get(str(code), [])


class FakeOUI:
    def __init__(self, path: str, debug: bool = False):
        self.path = path
        self.debug = debug

    def parse(self):
        return FakeOUIParsed()


# Inject fake external dependencies so importing pymacgen does not require them
# Fake pyoui
fake_pyoui = types.ModuleType("pyoui")
fake_pyoui.OUI = FakeOUI
fake_pyoui.OuiEntry = FakeOuiEntry
sys.modules["pyoui"] = fake_pyoui

# Fake loguru
class _FakeLogger:
    def error(self, *args, **kwargs):
        pass

fake_loguru = types.ModuleType("loguru")
fake_loguru.logger = _FakeLogger()
sys.modules["loguru"] = fake_loguru

import importlib
pymacgen = importlib.import_module("pymacgen")
MACGenerator = pymacgen.MACGenerator


def assert_is_full_mac(testcase: unittest.TestCase, mac: str):
    testcase.assertIsInstance(mac, str)
    testcase.assertRegex(mac, r"(?:[0-9A-F]{2}:){5}[0-9A-F]{2}")


class TestMACGenerator(unittest.TestCase):
    def test_generate_last_six_format_and_uppercase(self):
        part = MACGenerator._generate_last_six()
        self.assertRegex(part, r"[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}")
        self.assertEqual(part, part.upper())

    def test_by_mac_keeps_prefix_and_returns_full_mac(self):
        out = MACGenerator.by_mac("EA:7B:EE:FB:01:42")
        self.assertTrue(out.startswith("EA:7B:EE:"))
        assert_is_full_mac(self, out)

    def test_by_prefix_keeps_prefix_and_returns_full_mac(self):
        out = MACGenerator.by_prefix("42:06:66")
        self.assertTrue(out.startswith("42:06:66:"))
        assert_is_full_mac(self, out)

    def test_by_organization_uses_oui_lookup(self):
        mg = MACGenerator("/dev/null", debug=True)
        out = mg.by_organization("Apple")  # case-insensitive lookup
        self.assertTrue(out.startswith("AA:BB:CC:"))
        assert_is_full_mac(self, out)

    def test_by_country_name_found(self):
        mg = MACGenerator("/dev/null")
        for country_name, expected_prefix in (("Germany", "DE:AD:BE"), ("United States", "FE:ED:FA")):
            with self.subTest(country_name=country_name):
                out = mg.by_country_name(country_name)
                self.assertTrue(out.startswith(expected_prefix + ":"))
                assert_is_full_mac(self, out)

    def test_by_country_name_not_found_returns_none(self):
        mg = MACGenerator("/dev/null")
        out = mg.by_country_name("NowhereLand")
        self.assertIsNone(out)

    def test_by_country_code_found(self):
        mg = MACGenerator("/dev/null")
        for code, expected_prefix in (("DE", "DE:00:00"), ("US", "FA:CE:00")):
            with self.subTest(code=code):
                out = mg.by_country_code(code)
                self.assertTrue(out.startswith(expected_prefix + ":"))
                assert_is_full_mac(self, out)

    def test_by_country_code_not_found_returns_none(self):
        mg = MACGenerator("/dev/null")
        out = mg.by_country_code("DK")
        self.assertIsNone(out)


if __name__ == "__main__":
    unittest.main()
