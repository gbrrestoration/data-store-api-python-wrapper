# rrap_mds_is_data_api.AccessCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_admin_access_check_access_check_admin_access_get**](AccessCheckApi.md#check_admin_access_check_access_check_admin_access_get) | **GET** /check-access/check-admin-access | Check Admin Access
[**check_general_access_check_access_check_general_access_get**](AccessCheckApi.md#check_general_access_check_access_check_general_access_get) | **GET** /check-access/check-general-access | Check General Access
[**check_read_access_check_access_check_read_access_get**](AccessCheckApi.md#check_read_access_check_access_check_read_access_get) | **GET** /check-access/check-read-access | Check Read Access
[**check_write_access_check_access_check_write_access_get**](AccessCheckApi.md#check_write_access_check_access_check_write_access_get) | **GET** /check-access/check-write-access | Check Write Access


# **check_admin_access_check_access_check_admin_access_get**
> User check_admin_access_check_access_check_admin_access_get()

Check Admin Access

Function Description --------------------  A check point for the data store which responds if any authentication  is present and valid. Checks the the user is an admin.  Arguments ---------- user : User, optional     The authenticated user - may or may not have the correct roles.   Returns ------- User     Returns user information    See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import access_check_api
from rrap_mds_is_data_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check Admin Access
        api_response = api_instance.check_admin_access_check_access_check_admin_access_get()
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_admin_access_check_access_check_admin_access_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **check_general_access_check_access_check_general_access_get**
> User check_general_access_check_access_check_general_access_get()

Check General Access

Function Description --------------------  A check point for the data store which responds if any authentication  is present and valid. Does not check role authorisation.  Used to distinguish between 'general' and 'protected' access for this API.    Arguments ---------- user : User, optional     The authenticated user - may or may not have the correct roles.   Returns ------- User     Returns user information    See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import access_check_api
from rrap_mds_is_data_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check General Access
        api_response = api_instance.check_general_access_check_access_check_general_access_get()
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_general_access_check_access_check_general_access_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **check_read_access_check_access_check_read_access_get**
> User check_read_access_check_access_check_read_access_get()

Check Read Access

Function Description --------------------  A check point for the data store front end to validate authorisation.  Only allows read users (or read and write).   Arguments ---------- protected_roles : ProtectedRole, optional     The protected role dependency, by default Depends( kc_auth.get_any_protected_role_dependency([usage_role]))  Returns ------- User     Returns user information   See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import access_check_api
from rrap_mds_is_data_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check Read Access
        api_response = api_instance.check_read_access_check_access_check_read_access_get()
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_read_access_check_access_check_read_access_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **check_write_access_check_access_check_write_access_get**
> User check_write_access_check_access_check_write_access_get()

Check Write Access

Function Description --------------------  A check point for the data store front end to validate authorisation.  Only allows read-write users.   Arguments ---------- protected_roles : ProtectedRole, optional     The protected role dependency, by default Depends( kc_auth.get_any_protected_role_dependency([usage_role]))  Returns ------- User     Returns user information    See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_data_api
from rrap_mds_is_data_api.api import access_check_api
from rrap_mds_is_data_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check Write Access
        api_response = api_instance.check_write_access_check_access_check_write_access_get()
        pprint(api_response)
    except rrap_mds_is_data_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_write_access_check_access_check_write_access_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

