from pymacgen import MACGenerator
# from pyoui import OUI  # todo crosscheck

# these do not need instantiation of the MACGenerator class
print(MACGenerator.by_mac(str("EA:7B:EE:FB:01:42")))
print(MACGenerator.by_prefix("42:06:66"))

# these utilize the pyoui library, so instantiation of the MACGenerator class is needed
m = MACGenerator("/tmp/oui.txt", True)

# by organization name examples
for on in ["national security agency", "samsung", "nokia", "apple"]:
    print("Organization Name: '{0}' |", m.by_organization(on))

# by country name examples
for cc in ["DE", "CN", "US", "DK"]:
    print("Country Code: '{0}' |".format(cc), m.by_country_code(cc))

# by country code examples
for cn in ["Germany", "China", "United States", "Denmark"]:
    print("Country Name: '{0}' |".format(cn), m.by_country_name(cn))
