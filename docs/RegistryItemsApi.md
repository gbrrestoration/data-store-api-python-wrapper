# rrap_mds_is_data_api.RegistryItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_dataset**](RegistryItemsApi.md#fetch_dataset) | **GET** /registry/items/fetch-dataset | Fetch Dataset
[**list_all_datasets**](RegistryItemsApi.md#list_all_datasets) | **GET** /registry/items/list-all-datasets | List All Datasets


# **fetch_dataset**
> RegistryFetchResponse fetch_dataset(handle_id)

Fetch Dataset

fetch_dataset Given a unique Handle ID, this function searches the data registry for  the data associated with this handle and will return a RegistryFetchResponse  containing as RegistryItem as an attribute for the queried  dataset.  Arguments ---------- handle_id : str     The unique handle ID for searching the data-registry with.  Returns -------  : RegistryFetchResponse     Containing the response status and registry_item.  Raises ------ HTTPException     If fails to source item from the registry.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import registry_items_api
from rrap_mds_is_data_api.model.registry_fetch_response import RegistryFetchResponse
from rrap_mds_is_data_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_data_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_data_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_data_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registry_items_api.RegistryItemsApi(api_client)
    handle_id = "handle_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch Dataset
        api_response = api_instance.fetch_dataset(handle_id)
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling RegistryItemsApi->fetch_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle_id** | **str**|  |

### Return type

[**RegistryFetchResponse**](RegistryFetchResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_datasets**
> ListRegistryResponse list_all_datasets()

List All Datasets

list_all_datasets Lists all data in the data registry. Returns a ListRegistryResponse with a registry_items attribute  which is a python list of RegistryItem objects, one object per entry to the registry.  Returns -------  : ListRegistryResponse     An object containing the responses status and a registry_items python list containing a RegistryItem for      each item in the the database.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import registry_items_api
from rrap_mds_is_data_api.model.list_registry_response import ListRegistryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_data_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_data_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_data_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registry_items_api.RegistryItemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List All Datasets
        api_response = api_instance.list_all_datasets()
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling RegistryItemsApi->list_all_datasets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRegistryResponse**](ListRegistryResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

