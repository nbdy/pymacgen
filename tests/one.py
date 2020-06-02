from pymacgen import MACGenerator

# these do not need instantiation of the MACGenerator class
print(MACGenerator.by_mac(str("EA:7B:EE:FB:01:42")))
print(MACGenerator.by_prefix("42:06:66"))

# these utilize the pyoui library, so instantiation of the MACGenerator class is needed
m = MACGenerator("/tmp/oui.txt", True)

# by company name examples
print(m.by_organization("national security agency"))
print(m.by_organization("samsung"))

# by country name examples
print(m.by_country_code("DE"))
print(m.by_country_code("CN"))

# by country code examples
print(m.by_country_name("Germany"))
print(m.by_country_name("China"))
