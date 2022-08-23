"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from rrap_mds_is_data_api.api_client import ApiClient, Endpoint as _Endpoint
from rrap_mds_is_data_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from rrap_mds_is_data_api.model.credential_response import CredentialResponse
from rrap_mds_is_data_api.model.credentials_request import CredentialsRequest
from rrap_mds_is_data_api.model.http_validation_error import HTTPValidationError


class RegistryCredentialsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post_endpoint = _Endpoint(
            settings={
                'response_type': (CredentialResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/registry/credentials/generate-read-access-credentials',
                'operation_id': 'generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'credentials_request',
                ],
                'required': [
                    'credentials_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'credentials_request':
                        (CredentialsRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'credentials_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post_endpoint = _Endpoint(
            settings={
                'response_type': (CredentialResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/registry/credentials/generate-write-access-credentials',
                'operation_id': 'generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'credentials_request',
                ],
                'required': [
                    'credentials_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'credentials_request':
                        (CredentialsRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'credentials_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post(
        self,
        credentials_request,
        **kwargs
    ):
        """Generate Read Access Credentials  # noqa: E501

        generate_access_credentials Given an S3 location, will attempt to generate programmatic access keys for the storage bucket at this particular subdirectory.   Note that the permission boundary is restricted by the intersection of  the preformed role and the created policy based on the location - which is bounded to the storage bucket.  This produces read level access into the subset of the bucket  requested in the S3 location object.  TODO currently this does not enforce any ownership of datasets.  Arguments ---------- credentials_request: CredentialsRequest      Contains the location + console session URL required flag  Returns -------  : CredentialResponse     The AWS credentials  Raises ------ HTTPException     500 error code if something goes wrong with STS call or otherwise.  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post(credentials_request, async_req=True)
        >>> result = thread.get()

        Args:
            credentials_request (CredentialsRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CredentialResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['credentials_request'] = \
            credentials_request
        return self.generate_read_access_credentials_registry_credentials_generate_read_access_credentials_post_endpoint.call_with_http_info(**kwargs)

    def generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post(
        self,
        credentials_request,
        **kwargs
    ):
        """Generate Write Access Credentials  # noqa: E501

        generate_access_credentials Given an S3 location, will attempt to generate programmatic access keys for the storage bucket at this particular subdirectory.   Note that the permission boundary is restricted by the intersection of  the preformed role and the created policy based on the location - which is bounded to the storage bucket.  This produces write level access into the subset of the bucket  requested in the S3 location object.  TODO currently this does not enforce any ownership of datasets.  Arguments ---------- credentials_request: CredentialsRequest      Contains the location + console session URL required flag  Returns -------  : CredentialResponse     The AWS credentials  Raises ------ HTTPException     500 error code if something goes wrong with STS call or otherwise.  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post(credentials_request, async_req=True)
        >>> result = thread.get()

        Args:
            credentials_request (CredentialsRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CredentialResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['credentials_request'] = \
            credentials_request
        return self.generate_write_access_credentials_registry_credentials_generate_write_access_credentials_post_endpoint.call_with_http_info(**kwargs)

