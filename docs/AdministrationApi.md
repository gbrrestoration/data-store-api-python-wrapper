# openapi_client.AdministrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post**](AdministrationApi.md#convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post) | **POST** /admin/registry/convert/collection-format/ro-crate | Convert Collection Format Rocrate
[**convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post**](AdministrationApi.md#convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post) | **POST** /admin/registry/convert/rocrate/collection-format | Convert Rocrate Collection Format
[**export_registry_parsed_admin_registry_export_parsed_get**](AdministrationApi.md#export_registry_parsed_admin_registry_export_parsed_get) | **GET** /admin/registry/export/parsed | Export Registry Parsed
[**export_registry_unparsed_admin_registry_export_unparsed_get**](AdministrationApi.md#export_registry_unparsed_admin_registry_export_unparsed_get) | **GET** /admin/registry/export/unparsed | Export Registry Unparsed
[**import_registry_parsed_admin_registry_import_parsed_post**](AdministrationApi.md#import_registry_parsed_admin_registry_import_parsed_post) | **POST** /admin/registry/import/parsed | Import Registry Parsed
[**import_registry_unparsed_admin_registry_import_unparsed_post**](AdministrationApi.md#import_registry_unparsed_admin_registry_import_unparsed_post) | **POST** /admin/registry/import/unparsed | Import Registry Unparsed


# **convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post**
> ResponseConvertCollectionFormatRocrate convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post(input_convert_collection_format_rocrate)

Convert Collection Format Rocrate

convert_collection_format_rocrate Given a list of collection format inputs will attempt to return a list  of freshly generated ro-crate objects. Note that the collection format  alone is not sufficient since it does not include the registry metadata such as the s3 location, created time etc. For this reason the input  type also includes some other helper fields likely sourced from the  registry item.  Arguments ---------- collection_format_input_list : InputConvertCollectionFormatRocrate     The list of collection formats  Returns -------  : ResponseConvertCollectionFormatRocrate     The list of outputted possible rocrates.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.response_convert_collection_format_rocrate import ResponseConvertCollectionFormatRocrate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.input_convert_collection_format_rocrate import InputConvertCollectionFormatRocrate
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
    api_instance = administration_api.AdministrationApi(api_client)
    input_convert_collection_format_rocrate = InputConvertCollectionFormatRocrate(
        collection_format_items=[
            CollectionFormatConversion(
                handle="handle_example",
                collection_format=CollectionFormat(
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
                ),
                s3=S3Location(
                    bucket_name="bucket_name_example",
                    path="path_example",
                    s3_uri="s3_uri_example",
                ),
                created_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
    ) # InputConvertCollectionFormatRocrate | 

    # example passing only required values which don't have defaults set
    try:
        # Convert Collection Format Rocrate
        api_response = api_instance.convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post(input_convert_collection_format_rocrate)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_convert_collection_format_rocrate** | [**InputConvertCollectionFormatRocrate**](InputConvertCollectionFormatRocrate.md)|  |

### Return type

[**ResponseConvertCollectionFormatRocrate**](ResponseConvertCollectionFormatRocrate.md)

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

# **convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post**
> ResponseConvertRocrateCollectionFormat convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post(input_convert_rocrate_collection_format)

Convert Rocrate Collection Format

convert_rocrate_collection_format Given a list of rocrate items will return a list of equal size with items in the same order. Each item represents a possible successful conversion into a collection format object. Each item includes an error field True/False for whether the conversion succeeds, a collection_format if it does and an error_message if it doesn't.  This method is designed to assist database migrations from the admin tools by providing the means to generate up to date collection format representations against the current schema. This can be used in conjunction with imports/exports to perform a quick database update.  Arguments ---------- rocrate_input_list : InputConvertRocrateCollectionFormat     The list of rocrate inputs  Returns -------  : ResponseConvertRocrateCollectionFormat     The list of possible collection format outputs  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.response_convert_rocrate_collection_format import ResponseConvertRocrateCollectionFormat
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.input_convert_rocrate_collection_format import InputConvertRocrateCollectionFormat
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
    api_instance = administration_api.AdministrationApi(api_client)
    input_convert_rocrate_collection_format = InputConvertRocrateCollectionFormat(
        rocrate_items=[
            {},
        ],
    ) # InputConvertRocrateCollectionFormat | 

    # example passing only required values which don't have defaults set
    try:
        # Convert Rocrate Collection Format
        api_response = api_instance.convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post(input_convert_rocrate_collection_format)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_convert_rocrate_collection_format** | [**InputConvertRocrateCollectionFormat**](InputConvertRocrateCollectionFormat.md)|  |

### Return type

[**ResponseConvertRocrateCollectionFormat**](ResponseConvertRocrateCollectionFormat.md)

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

# **export_registry_parsed_admin_registry_export_parsed_get**
> RegistryParsedExport export_registry_parsed_admin_registry_export_parsed_get()

Export Registry Parsed

export_registry_parsed Returns all the registry items parsed into the current RegistryItem format.  Returns -------  : RegistryParsedExport     The export object which has a list of entries.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.registry_parsed_export import RegistryParsedExport
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
    api_instance = administration_api.AdministrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export Registry Parsed
        api_response = api_instance.export_registry_parsed_admin_registry_export_parsed_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->export_registry_parsed_admin_registry_export_parsed_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistryParsedExport**](RegistryParsedExport.md)

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

# **export_registry_unparsed_admin_registry_export_unparsed_get**
> RegistryUnparsedExport export_registry_unparsed_admin_registry_export_unparsed_get()

Export Registry Unparsed

export_registry_unparsed Returns all the registry items without first parsing them as RegistryItems. This method is useful for a situation in which the items in the registry are no longer valid under the current RegistryItem model. You can use this method to dump the db, then modify it offline to be valid, then upload it using the parsed import endpoint to validate that the new entries are valid and are updating old entries as desired.  Returns -------  : RegistryUnparsedExport     The list of unparsed objects in Dict[str,Any] format.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.registry_unparsed_export import RegistryUnparsedExport
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
    api_instance = administration_api.AdministrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export Registry Unparsed
        api_response = api_instance.export_registry_unparsed_admin_registry_export_unparsed_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->export_registry_unparsed_admin_registry_export_unparsed_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistryUnparsedExport**](RegistryUnparsedExport.md)

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

# **import_registry_parsed_admin_registry_import_parsed_post**
> ImportResponse import_registry_parsed_admin_registry_import_parsed_post(registry_parsed_import)

Import Registry Parsed

import_registry_parsed Given a list of registry items (parsed as valid before being accepted at this endpoint) this method will update the current registry, according to the rules you set in the other options, to match your import. This method is much safer than the unparsed method as it only allows valid RegistryItems in. However there could be situations where you want to preemptively update the registry before the API is updated to remove down time after update. See the options in ImportResponse, these are critical controls.  Arguments ---------- registry_import : RegistryParsedImport     The registry import object which contains configuration     options and the list of items. protected_roles : ProtectedRole, optional     _description_, by default Depends( admin_user_protected_role_dependency)  Returns -------  : ImportResponse     The response, which includes status info, statistics and     other items.  Raises ------ HTTPException     500 error if write failure occurs HTTPException     500 error if delete failure occurs  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.import_response import ImportResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.registry_parsed_import import RegistryParsedImport
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
    api_instance = administration_api.AdministrationApi(api_client)
    registry_parsed_import = RegistryParsedImport(
        items=[
            RegistryItem(
                handle="handle_example",
                collection_format=CollectionFormat(
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
                ),
                rocrate_metadata={},
                s3=S3Location(
                    bucket_name="bucket_name_example",
                    path="path_example",
                    s3_uri="s3_uri_example",
                ),
                created_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        allow_new_entries=False,
        allow_entry_deletion=False,
        trial_mode=False,
    ) # RegistryParsedImport | 

    # example passing only required values which don't have defaults set
    try:
        # Import Registry Parsed
        api_response = api_instance.import_registry_parsed_admin_registry_import_parsed_post(registry_parsed_import)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->import_registry_parsed_admin_registry_import_parsed_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_parsed_import** | [**RegistryParsedImport**](RegistryParsedImport.md)|  |

### Return type

[**ImportResponse**](ImportResponse.md)

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

# **import_registry_unparsed_admin_registry_import_unparsed_post**
> ImportResponse import_registry_unparsed_admin_registry_import_unparsed_post(registry_unparsed_import)

Import Registry Unparsed

import_registry_unparsed Given a list of unparsed - unvalidated -registry items this method will update the current registry, according to the rules you set in the other options, to match your import. This method is much less safe vs the unparsed method as it allows any valid dynamodb record as RegistryItems. However there could be situations where you want to pre-emptively update the registry before the API is updated to remove down time after update. See the options in ImportResponse, these are critical controls.  Arguments ---------- registry_import : RegistryParsedImport     The registry import object which contains configuration     options and the list of items. protected_roles : ProtectedRole, optional     _description_, by default Depends( admin_user_protected_role_dependency)  Returns -------  : ImportResponse     The response, which includes status info, statistics and     other items.  Raises ------ HTTPException     500 error if write failure occurs HTTPException     500 error if delete failure occurs  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import administration_api
from openapi_client.model.import_response import ImportResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.registry_unparsed_import import RegistryUnparsedImport
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
    api_instance = administration_api.AdministrationApi(api_client)
    registry_unparsed_import = RegistryUnparsedImport(
        items=[
            {},
        ],
        allow_new_entries=False,
        allow_entry_deletion=False,
        trial_mode=False,
    ) # RegistryUnparsedImport | 

    # example passing only required values which don't have defaults set
    try:
        # Import Registry Unparsed
        api_response = api_instance.import_registry_unparsed_admin_registry_import_unparsed_post(registry_unparsed_import)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationApi->import_registry_unparsed_admin_registry_import_unparsed_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_unparsed_import** | [**RegistryUnparsedImport**](RegistryUnparsedImport.md)|  |

### Return type

[**ImportResponse**](ImportResponse.md)

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

