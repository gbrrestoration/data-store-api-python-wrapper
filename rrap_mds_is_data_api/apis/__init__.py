
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from rrap_mds_is_data_api.api.access_check_api import AccessCheckApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from rrap_mds_is_data_api.api.access_check_api import AccessCheckApi
from rrap_mds_is_data_api.api.administration_api import AdministrationApi
from rrap_mds_is_data_api.api.metadata_api import MetadataApi
from rrap_mds_is_data_api.api.register_dataset_api import RegisterDatasetApi
from rrap_mds_is_data_api.api.registry_items_api import RegistryItemsApi
from rrap_mds_is_data_api.api.registry_credentials_api import RegistryCredentialsApi
from rrap_mds_is_data_api.api.default_api import DefaultApi
