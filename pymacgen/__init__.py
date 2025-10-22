from pyoui import OUI, OuiEntry
from loguru import logger as log
from random import getrandbits


class MACGenerator(object):
    oui = None
    debug = False

    def __init__(self, oui_file="/tmp/oui.txt", debug=False):
        self.oui = OUI(oui_file, debug).parse()
        self.debug = debug

    @staticmethod
    def _generate_last_six():
        # Generate three random octets as uppercase hex pairs separated by ':'
        return ":".join(f"{getrandbits(8):02X}" for _ in range(3))

    @classmethod
    def _generate_from_prefix(cls, prefix):
        if isinstance(prefix, OuiEntry):
            prefix = prefix.prefix
        if not prefix.endswith(":"):
            prefix += ":"
        return prefix + cls._generate_last_six()

    def _generate_from_entry(self, e: OuiEntry):
        return self._generate_from_prefix(e.prefix)

    def by_organization(self, name):
        e = next(iter(self.oui.by_organization(name)), None)
        if e is None:
            log.error("could not find any entries by organization '{0}'.".format(name))
            return None
        return self._generate_from_entry(e)

    @classmethod
    def by_mac(cls, mac: str):
        return cls._generate_from_prefix(mac[0:8])

    @classmethod
    def by_prefix(cls, prefix):
        return cls._generate_from_prefix(prefix)

    def by_country_name(self, name):
        e = next(iter(self.oui.by_country_name(name)), None)
        if e is None:
            log.error("could not find any entries by country name '{0}'.".format(name))
            return None
        return self._generate_from_entry(e)

    def by_country_code(self, code):
        e = next(iter(self.oui.by_country_code(code)), None)
        if e is None:
            log.error("could not find any entries by country code '{0}'.".format(code))
            return None
        return self._generate_from_entry(e)


__all__ = ["MACGenerator"]
