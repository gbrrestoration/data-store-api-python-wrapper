# openapi_client.RegistryCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post**](RegistryCredentialsApi.md#generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post) | **POST** /registry/credentials/generate-read-access-credentials | Generate Read Access Credentials
[**generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post**](RegistryCredentialsApi.md#generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post) | **POST** /registry/credentials/generate-write-access-credentials | Generate Write Access Credentials


# **generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post**
> CredentialResponse generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post(credentials_request)

Generate Read Access Credentials

generate_access_credentials Given an S3 location, will attempt to generate programmatic access keys for the storage bucket at this particular subdirectory.   Note that the permission boundary is restricted by the intersection of  the preformed role and the created policy based on the location - which is bounded to the storage bucket.  This produces read level access into the subset of the bucket  requested in the S3 location object.  TODO currently this does not enforce any ownership of datasets.  Arguments ---------- credentials_request: CredentialsRequest      Contains the location + console session URL required flag  Returns -------  : CredentialResponse     The AWS credentials  Raises ------ HTTPException     500 error code if something goes wrong with STS call or otherwise.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import registry_credentials_api
from openapi_client.model.credentials_request import CredentialsRequest
from openapi_client.model.credential_response import CredentialResponse
from openapi_client.model.http_validation_error import HTTPValidationError
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
    api_instance = registry_credentials_api.RegistryCredentialsApi(api_client)
    credentials_request = CredentialsRequest(
        s3_location=S3Location(
            bucket_name="bucket_name_example",
            path="path_example",
            s3_uri="s3_uri_example",
        ),
        console_session_required=True,
    ) # CredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Read Access Credentials
        api_response = api_instance.generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post(credentials_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistryCredentialsApi->generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  |

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

# **generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post**
> CredentialResponse generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post(credentials_request)

Generate Write Access Credentials

generate_access_credentials Given an S3 location, will attempt to generate programmatic access keys for the storage bucket at this particular subdirectory.   Note that the permission boundary is restricted by the intersection of  the preformed role and the created policy based on the location - which is bounded to the storage bucket.  This produces write level access into the subset of the bucket  requested in the S3 location object.  TODO currently this does not enforce any ownership of datasets.  Arguments ---------- credentials_request: CredentialsRequest      Contains the location + console session URL required flag  Returns -------  : CredentialResponse     The AWS credentials  Raises ------ HTTPException     500 error code if something goes wrong with STS call or otherwise.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import registry_credentials_api
from openapi_client.model.credentials_request import CredentialsRequest
from openapi_client.model.credential_response import CredentialResponse
from openapi_client.model.http_validation_error import HTTPValidationError
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
    api_instance = registry_credentials_api.RegistryCredentialsApi(api_client)
    credentials_request = CredentialsRequest(
        s3_location=S3Location(
            bucket_name="bucket_name_example",
            path="path_example",
            s3_uri="s3_uri_example",
        ),
        console_session_required=True,
    ) # CredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Write Access Credentials
        api_response = api_instance.generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post(credentials_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistryCredentialsApi->generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  |

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

