"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.collection_format import CollectionFormat
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.mint_response import MintResponse
from openapi_client.model.update_metadata_response import UpdateMetadataResponse


class RegisterDatasetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_dataset_schema_register_update_metadata_post_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateMetadataResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/register/update-metadata',
                'operation_id': 'get_dataset_schema_register_update_metadata_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'handle_id',
                    'collection_format',
                ],
                'required': [
                    'handle_id',
                    'collection_format',
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
                    'handle_id':
                        (str,),
                    'collection_format':
                        (CollectionFormat,),
                },
                'attribute_map': {
                    'handle_id': 'handle_id',
                },
                'location_map': {
                    'handle_id': 'query',
                    'collection_format': 'body',
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
        self.mint_dataset_register_mint_dataset_post_endpoint = _Endpoint(
            settings={
                'response_type': (MintResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/register/mint-dataset',
                'operation_id': 'mint_dataset_register_mint_dataset_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_format',
                ],
                'required': [
                    'collection_format',
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
                    'collection_format':
                        (CollectionFormat,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'collection_format': 'body',
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

    def get_dataset_schema_register_update_metadata_post(
        self,
        handle_id,
        collection_format,
        **kwargs
    ):
        """Get Dataset Schema  # noqa: E501

        get_dataset_schema Given the metadata and handle id, will re-parse the metadata as valid ro crate, then overwrite the registry entry and  s3 bucket metadata.  Will also update the timestamp of the updated_time to be  the current time.  Arguments ---------- collection_format : CollectionFormat     The updated metadata handle_id : str     The handle for which to update the metadata  Returns -------  : UpdateMetadataResponse     The updated metadata response  Raises ------ HTTPException     422 - validation failure against schema at API level HTTPException     400 - validation failure against schema at JSON schema level HTTPException     400 - failed to transform into ro crate HTTPException     500 - failed to update registry   See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dataset_schema_register_update_metadata_post(handle_id, collection_format, async_req=True)
        >>> result = thread.get()

        Args:
            handle_id (str):
            collection_format (CollectionFormat):

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
            UpdateMetadataResponse
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
        kwargs['handle_id'] = \
            handle_id
        kwargs['collection_format'] = \
            collection_format
        return self.get_dataset_schema_register_update_metadata_post_endpoint.call_with_http_info(**kwargs)

    def mint_dataset_register_mint_dataset_post(
        self,
        collection_format,
        **kwargs
    ):
        """Mint Dataset  # noqa: E501

        Function Description --------------------  Used by the front end to prepare the data store, the handle service, metadata etc for a new dataset. Accepts the filled out metadata which must validate  against the current dataset schema which is provided by the /dataset-schema endpoint.  If the schema validates, then a handle will be minted, a handle endpoint will be formed  and updated for the handle service, a S3 location will be determined, the metadata updated with these details and uploaded to that location to seed the folder structure.   This function returns the MintResponse which includes the status, the handle, the S3 location information.   Arguments ---------- collection_format : CollectionFormat     The input pre-parsed using the pydantic input model validation.     Still is validated using the json schema as well.  Returns ------- MintResponse     The mint response object which encodes the result if successful   Raises ------ HTTPException     400 response if metadata fails to validate HTTPException     400 response if the S3 location cannot be uniquely determined  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mint_dataset_register_mint_dataset_post(collection_format, async_req=True)
        >>> result = thread.get()

        Args:
            collection_format (CollectionFormat):

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
            MintResponse
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
        kwargs['collection_format'] = \
            collection_format
        return self.mint_dataset_register_mint_dataset_post_endpoint.call_with_http_info(**kwargs)

