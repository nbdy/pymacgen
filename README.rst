
pymacgen
--------

generates mac addresses

how to..
^^^^^^^^

... install
~~~~~~~~~~~

```shell script

from github
===========

pip3 install git+https://github.com/smthnspcl/pymacgen

if this repo has been cloned
============================

pip3 install .

.. code-block::

   #### ... use from cli
   ```shell script
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

... use from code
~~~~~~~~~~~~~~~~~

.. code-block:: python


