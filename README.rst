pymacgen
--------

generates mac addresses

.. _how-to:

how to..
~~~~~~~~

.. _-install:

... install
^^^^^^^^^^^

.. code:: shell

   # from pypi
   pip3 install pymacgen
   # from github
   pip3 install git+https://github.com/smthnspcl/pymacgen
   # if this repo has been cloned
   pip3 install .

.. _-use-from-cli:

... use from cli
^^^^^^^^^^^^^^^^

.. code:: shell

   pymacgen --help
   usage: pymacgen [-h] [-o OUI] [-d] [-on ORGANIZATION_NAME] [-mp MAC_PREFIX] [-cn COUNTRY_NAME] [-g GENERATE]

   optional arguments:
     -h, --help            show this help message and exit
     -o OUI, --oui OUI     path to oui file; will be downloaded if not found
     -d, --debug           enable debugging
     -on ORGANIZATION_NAME, --organization-name ORGANIZATION_NAME
                           search by organization name; case insensitive
     -mp MAC_PREFIX, --mac-prefix MAC_PREFIX
                           search by mac prefix; 00-00-00 or 00:00:00 or 000000
     -cn COUNTRY_NAME, --country-name COUNTRY_NAME
                           search by country name; case insensitive
     -g GENERATE, --generate GENERATE
                           generate a random mac address or by found prefix

.. _-use-from-code:

... use from code
^^^^^^^^^^^^^^^^^

.. code:: python

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
