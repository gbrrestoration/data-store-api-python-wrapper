# openapi_client.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_schema_metadata_dataset_schema_get**](MetadataApi.md#get_dataset_schema_metadata_dataset_schema_get) | **GET** /metadata/dataset-schema | Get Dataset Schema
[**validate_metadata_metadata_validate_metadata_post**](MetadataApi.md#validate_metadata_metadata_validate_metadata_post) | **POST** /metadata/validate-metadata | Validate Metadata


# **get_dataset_schema_metadata_dataset_schema_get**
> Schema get_dataset_schema_metadata_dataset_schema_get()

Get Dataset Schema

Function Description --------------------  Returns the json schema Schema object which defines the required dataset metadata.  Metdata which is uploaded via the mint-dataset endpoint will be validated against this  schema before being accepted.   Arguments ---------- protected_roles : ProtectedRole, optional     by default Depends( kc_auth.get_any_protected_role_dependency([usage_role]))  Returns ------- Schema     The json schema object   Raises ------ HTTPException     Raises a 500 internal error if something goes wrong.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import metadata_api
from openapi_client.model.schema import Schema
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Dataset Schema
        api_response = api_instance.get_dataset_schema_metadata_dataset_schema_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataApi->get_dataset_schema_metadata_dataset_schema_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Schema**](Schema.md)

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

# **validate_metadata_metadata_validate_metadata_post**
> Status validate_metadata_metadata_validate_metadata_post(collection_format)

Validate Metadata

validate_metadata Allows for validation checks without any interaction with external resources. Used for testing and potentially as an ongoing validation checker on the front end.  Arguments ---------- metadata : CollectionFormat     The metadata to validate - this validation occurs both in terms of      parsing the collection format object at the API level and also by      validating the schema against the json schema file.  Returns -------  : Status     The status object - true/false  Raises ------ HTTPException 422     If the parsing fails at API level then 422 is returned with the      shared interface validation exception type.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import metadata_api
from openapi_client.model.status import Status
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.collection_format import CollectionFormat
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
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
        # Validate Metadata
        api_response = api_instance.validate_metadata_metadata_validate_metadata_post(collection_format)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataApi->validate_metadata_metadata_validate_metadata_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_format** | [**CollectionFormat**](CollectionFormat.md)|  |

### Return type

[**Status**](Status.md)

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

