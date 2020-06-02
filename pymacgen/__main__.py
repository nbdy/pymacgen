from argparse import ArgumentParser
from pymacgen import MACGenerator
from loguru import logger as log


def main():
    ap = ArgumentParser()
    ap.add_argument("-o", "--oui", default="/tmp/oui.txt", help="path to oui file; will be downloaded if not found")
    ap.add_argument("-d", "--debug", action="store_true", help="enable debugging")
    ap.add_argument("-org", "--organization", help="search by organization name; case insensitive")
    ap.add_argument("-mp", "--mac-prefix", help="search by mac prefix; 00-00-00 or 00:00:00 or 000000")
    ap.add_argument("-cn", "--country-name", help="search by country name; case insensitive")
    ap.add_argument("-cc", "--country-code", help="search by country code")
    ap.add_argument("-g", "--generate", help="generate a random mac address or by found prefix")
    a = ap.parse_args()

    mg = MACGenerator(a.oui, a.debug)
    i = None
    if a.organization_name is not None:
        i = mg.by_organization(a.organization)
    elif a.mac_prefix is not None:
        i = mg.by_prefix(a.mac_prefix)
    elif a.country_name is not None:
        i = mg.by_country_name(a.country_name)
    elif a.country_code is not None:
        i = mg.by_country_code(a.country_code)

    if i is None:
        log.error("could not find mac info")
        exit()

    if a.generate:
        print(i)


if __name__ == '__main__':
    main()
