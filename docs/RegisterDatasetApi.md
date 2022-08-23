# rrap_mds_is_data_api.RegisterDatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_schema_register_update_metadata_post**](RegisterDatasetApi.md#get_dataset_schema_register_update_metadata_post) | **POST** /register/update-metadata | Get Dataset Schema
[**mint_dataset_register_mint_dataset_post**](RegisterDatasetApi.md#mint_dataset_register_mint_dataset_post) | **POST** /register/mint-dataset | Mint Dataset


# **get_dataset_schema_register_update_metadata_post**
> UpdateMetadataResponse get_dataset_schema_register_update_metadata_post(handle_id, collection_format)

Get Dataset Schema

get_dataset_schema Given the metadata and handle id, will re-parse the metadata as valid ro crate, then overwrite the registry entry and  s3 bucket metadata.  Will also update the timestamp of the updated_time to be  the current time.  Arguments ---------- collection_format : CollectionFormat     The updated metadata handle_id : str     The handle for which to update the metadata  Returns -------  : UpdateMetadataResponse     The updated metadata response  Raises ------ HTTPException     422 - validation failure against schema at API level HTTPException     400 - validation failure against schema at JSON schema level HTTPException     400 - failed to transform into ro crate HTTPException     500 - failed to update registry   See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import register_dataset_api
from rrap_mds_is_data_api.model.collection_format import CollectionFormat
from rrap_mds_is_data_api.model.update_metadata_response import UpdateMetadataResponse
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
    api_instance = register_dataset_api.RegisterDatasetApi(api_client)
    handle_id = "handle_id_example" # str | 
    collection_format = CollectionFormat(
        author=CollectionFormatAuthor(
            name="name_example",
            email="email_example",
            orcid="orcid_example",
            organisation=CollectionFormatOrganisation(
                name="name_example",
                ror="ror_example",
            ),
        ),
        dataset_info=CollectionFormatDatasetInfo(
            name="name_example",
            description="description_example",
            publisher=CollectionFormatOrganisation(
                name="name_example",
                ror="ror_example",
            ),
            created_date=dateutil_parser('1970-01-01').date(),
            published_date=dateutil_parser('1970-01-01').date(),
            license="license_example",
            keywords=[
                "keywords_example",
            ],
            version="version_example",
        ),
    ) # CollectionFormat | 

    # example passing only required values which don't have defaults set
    try:
        # Get Dataset Schema
        api_response = api_instance.get_dataset_schema_register_update_metadata_post(handle_id, collection_format)
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling RegisterDatasetApi->get_dataset_schema_register_update_metadata_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle_id** | **str**|  |
 **collection_format** | [**CollectionFormat**](CollectionFormat.md)|  |

### Return type

[**UpdateMetadataResponse**](UpdateMetadataResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_dataset_register_mint_dataset_post**
> MintResponse mint_dataset_register_mint_dataset_post(collection_format)

Mint Dataset

Function Description --------------------  Used by the front end to prepare the data store, the handle service, metadata etc for a new dataset. Accepts the filled out metadata which must validate  against the current dataset schema which is provided by the /dataset-schema endpoint.  If the schema validates, then a handle will be minted, a handle endpoint will be formed  and updated for the handle service, a S3 location will be determined, the metadata updated with these details and uploaded to that location to seed the folder structure.   This function returns the MintResponse which includes the status, the handle, the S3 location information.   Arguments ---------- collection_format : CollectionFormat     The input pre-parsed using the pydantic input model validation.     Still is validated using the json schema as well.  Returns ------- MintResponse     The mint response object which encodes the result if successful   Raises ------ HTTPException     400 response if metadata fails to validate HTTPException     400 response if the S3 location cannot be uniquely determined  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import register_dataset_api
from rrap_mds_is_data_api.model.collection_format import CollectionFormat
from rrap_mds_is_data_api.model.mint_response import MintResponse
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
    api_instance = register_dataset_api.RegisterDatasetApi(api_client)
    collection_format = CollectionFormat(
        author=CollectionFormatAuthor(
            name="name_example",
            email="email_example",
            orcid="orcid_example",
            organisation=CollectionFormatOrganisation(
                name="name_example",
                ror="ror_example",
            ),
        ),
        dataset_info=CollectionFormatDatasetInfo(
            name="name_example",
            description="description_example",
            publisher=CollectionFormatOrganisation(
                name="name_example",
                ror="ror_example",
            ),
            created_date=dateutil_parser('1970-01-01').date(),
            published_date=dateutil_parser('1970-01-01').date(),
            license="license_example",
            keywords=[
                "keywords_example",
            ],
            version="version_example",
        ),
    ) # CollectionFormat | 

    # example passing only required values which don't have defaults set
    try:
        # Mint Dataset
        api_response = api_instance.mint_dataset_register_mint_dataset_post(collection_format)
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling RegisterDatasetApi->mint_dataset_register_mint_dataset_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_format** | [**CollectionFormat**](CollectionFormat.md)|  |

### Return type

[**MintResponse**](MintResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

