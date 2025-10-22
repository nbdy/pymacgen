# pymacgen

Generate realistic MAC addresses from OUIs (vendors) or prefixes.

[![PyPI](https://img.shields.io/pypi/v/pymacgen.svg?label=PyPI&logo=pypi)](https://pypi.org/project/pymacgen/)
![Python Versions](https://img.shields.io/pypi/pyversions/pymacgen.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

## Installation

- Using pip (PyPI):
  - pip install pymacgen
- Using uv:
  - uv add pymacgen

## Quick start

- CLI (help):
  ```sh
  pymacgen --help
  ```
- Python (no OUI file needed for plain prefix/MAC):
  ```python
  from pymacgen import MACGenerator

  # Classmethods: generate using an existing MAC or a prefix (first 3 octets)
  print(MACGenerator.by_mac("EA:7B:EE:FB:01:42"))   # -> EA:7B:EE:AA:BB:CC
  print(MACGenerator.by_prefix("42:06:66"))         # -> 42:06:66:AA:BB:CC
  ```

## CLI usage

The CLI can search by organization, country name/code, or directly use a MAC prefix.
If the OUI file is not present at the given path, it will be downloaded automatically.

Common examples:

- Using a MAC prefix (supports 00:00:00, 00-00-00, or 000000):
  ```sh
  pymacgen -mp 42:06:66
  # 42:06:66:3A:9F:BC
  ```

- By organization name (case-insensitive):
  ```sh
  pymacgen -org Samsung --oui /tmp/oui.txt
  # E8:50:8B:12:34:56
  ```

- By country name:
  ```sh
  pymacgen -cn Germany --oui /tmp/oui.txt
  # 00:1A:2B:12:34:56
  ```

- By country code:
  ```sh
  pymacgen -cc DE --oui /tmp/oui.txt
  # 00:1A:2B:12:34:56
  ```

Tips:
- Add -d to enable debug logging.
- The output is randomized in the last three octets; running the same command again will produce a different MAC.

## Python usage

For organization/country queries you need an OUI database (handled by pyoui). Pass a path where the file can be stored; it will be downloaded if missing.

```python
from pymacgen import MACGenerator

# Classmethods: do not require instantiation
print(MACGenerator.by_mac("EA:7B:EE:FB:01:42"))     # keep OUI of existing MAC
print(MACGenerator.by_prefix("42:06:66"))           # generate from explicit prefix

# Instance methods: require an OUI file (auto-downloaded if not present)
m = MACGenerator("/tmp/oui.txt", debug=True)

# By organization name (case-insensitive)
print(m.by_organization("National Security Agency"))
print(m.by_organization("Samsung"))

# By country name
print(m.by_country_name("Germany"))
print(m.by_country_name("China"))

# By country code
print(m.by_country_code("DE"))
print(m.by_country_code("CN"))
```

Notes:
- Accepted prefix formats: AA:BB:CC, AA-BB-CC, or AABBCC.
- by_mac(...) preserves the first three octets from the given MAC and randomizes the rest.
- This package uses pyoui under the hood to resolve OUIs.

## License

MIT © 2020 Pascal Eberlein
