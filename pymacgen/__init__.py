from pyoui import OUI, OuiEntry
from string import hexdigits
from random import choice


class MACGenerator(object):
    oui = None
    debug = False

    def __init__(self, oui_file="/tmp/oui.txt", debug=False):
        self.oui = OUI(oui_file, debug).parse()
        self.debug = debug

    @staticmethod
    def _generate_last_six():
        r = ""
        for i in range(6):
            r += choice(hexdigits)
            if (i % 2) == 1:
                r += ":"
        r = r[0:-1]
        return r.upper()

    @classmethod
    def _generate_from_prefix(cls, prefix: str):
        if not prefix.endswith(":"):
            prefix += ":"
        return prefix + cls._generate_last_six()

    def _generate_from_entry(self, e: OuiEntry):
        return self._generate_from_prefix(e.prefix)

    def by_organization(self, name):  # todo by best matching
        return self._generate_from_entry(list(self.oui.by_organization(name))[0])

    @staticmethod
    def by_prefix(prefix):
        return MACGenerator._generate_from_prefix(prefix)

    def by_country_name(self, name):
        return self._generate_from_entry(list(self.oui.by_country_code(name))[0])

    def by_country_code(self, code):
        return self._generate_from_prefix(list(self.oui.by_country_code(code))[0])

    @staticmethod
    def by_mac(mac: str):
        return MACGenerator._generate_from_prefix(mac.replace(":", "")[0:6])


__all__ = ["MACGenerator"]
