from pyoui import OUI, OuiEntry
from loguru import logger as log
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
    def _generate_from_prefix(cls, prefix):
        if isinstance(prefix, OuiEntry):
            prefix = prefix.prefix
        if not prefix.endswith(":"):
            prefix += ":"
        return prefix + cls._generate_last_six()

    def _generate_from_entry(self, e: OuiEntry):
        return self._generate_from_prefix(e.prefix)

    def by_organization(self, name):  # todo by best matching
        return self._generate_from_entry(list(self.oui.by_organization(name))[0])

    @classmethod
    def by_mac(cls, mac: str):
        return cls._generate_from_prefix(mac[0:8])

    @classmethod
    def by_prefix(cls, prefix):
        return cls._generate_from_prefix(prefix)

    def by_country_name(self, name):
        try:
            return self._generate_from_entry(list(self.oui.by_country_name(name))[0])
        except IndexError:
            log.error("could not find any entries by country name '{0}'.".format(name))
            return None

    def by_country_code(self, code):
        try:
            return self._generate_from_prefix(list(self.oui.by_country_code(code))[0])
        except IndexError:
            log.error("could not find any entries by country code '{0}'.".format(code))
            return None


__all__ = ["MACGenerator"]
