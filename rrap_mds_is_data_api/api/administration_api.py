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
from rrap_mds_is_data_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_data_api.model.import_response import ImportResponse
from rrap_mds_is_data_api.model.input_convert_collection_format_rocrate import InputConvertCollectionFormatRocrate
from rrap_mds_is_data_api.model.input_convert_rocrate_collection_format import InputConvertRocrateCollectionFormat
from rrap_mds_is_data_api.model.registry_parsed_export import RegistryParsedExport
from rrap_mds_is_data_api.model.registry_parsed_import import RegistryParsedImport
from rrap_mds_is_data_api.model.registry_unparsed_export import RegistryUnparsedExport
from rrap_mds_is_data_api.model.registry_unparsed_import import RegistryUnparsedImport
from rrap_mds_is_data_api.model.response_convert_collection_format_rocrate import ResponseConvertCollectionFormatRocrate
from rrap_mds_is_data_api.model.response_convert_rocrate_collection_format import ResponseConvertRocrateCollectionFormat


class AdministrationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post_endpoint = _Endpoint(
            settings={
                'response_type': (ResponseConvertCollectionFormatRocrate,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/convert/collection-format/ro-crate',
                'operation_id': 'convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_convert_collection_format_rocrate',
                ],
                'required': [
                    'input_convert_collection_format_rocrate',
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
                    'input_convert_collection_format_rocrate':
                        (InputConvertCollectionFormatRocrate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_convert_collection_format_rocrate': 'body',
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
        self.convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post_endpoint = _Endpoint(
            settings={
                'response_type': (ResponseConvertRocrateCollectionFormat,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/convert/rocrate/collection-format',
                'operation_id': 'convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_convert_rocrate_collection_format',
                ],
                'required': [
                    'input_convert_rocrate_collection_format',
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
                    'input_convert_rocrate_collection_format':
                        (InputConvertRocrateCollectionFormat,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_convert_rocrate_collection_format': 'body',
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
        self.export_registry_parsed_admin_registry_export_parsed_get_endpoint = _Endpoint(
            settings={
                'response_type': (RegistryParsedExport,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/export/parsed',
                'operation_id': 'export_registry_parsed_admin_registry_export_parsed_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.export_registry_unparsed_admin_registry_export_unparsed_get_endpoint = _Endpoint(
            settings={
                'response_type': (RegistryUnparsedExport,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/export/unparsed',
                'operation_id': 'export_registry_unparsed_admin_registry_export_unparsed_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.import_registry_parsed_admin_registry_import_parsed_post_endpoint = _Endpoint(
            settings={
                'response_type': (ImportResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/import/parsed',
                'operation_id': 'import_registry_parsed_admin_registry_import_parsed_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'registry_parsed_import',
                ],
                'required': [
                    'registry_parsed_import',
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
                    'registry_parsed_import':
                        (RegistryParsedImport,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'registry_parsed_import': 'body',
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
        self.import_registry_unparsed_admin_registry_import_unparsed_post_endpoint = _Endpoint(
            settings={
                'response_type': (ImportResponse,),
                'auth': [
                    'OAuth2PasswordBearer'
                ],
                'endpoint_path': '/admin/registry/import/unparsed',
                'operation_id': 'import_registry_unparsed_admin_registry_import_unparsed_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'registry_unparsed_import',
                ],
                'required': [
                    'registry_unparsed_import',
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
                    'registry_unparsed_import':
                        (RegistryUnparsedImport,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'registry_unparsed_import': 'body',
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

    def convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post(
        self,
        input_convert_collection_format_rocrate,
        **kwargs
    ):
        """Convert Collection Format Rocrate  # noqa: E501

        convert_collection_format_rocrate Given a list of collection format inputs will attempt to return a list  of freshly generated ro-crate objects. Note that the collection format  alone is not sufficient since it does not include the registry metadata such as the s3 location, created time etc. For this reason the input  type also includes some other helper fields likely sourced from the  registry item.  Arguments ---------- collection_format_input_list : InputConvertCollectionFormatRocrate     The list of collection formats  Returns -------  : ResponseConvertCollectionFormatRocrate     The list of outputted possible rocrates.  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post(input_convert_collection_format_rocrate, async_req=True)
        >>> result = thread.get()

        Args:
            input_convert_collection_format_rocrate (InputConvertCollectionFormatRocrate):

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
            ResponseConvertCollectionFormatRocrate
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
        kwargs['input_convert_collection_format_rocrate'] = \
            input_convert_collection_format_rocrate
        return self.convert_collection_format_rocrate_admin_registry_convert_collection_format_ro_crate_post_endpoint.call_with_http_info(**kwargs)

    def convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post(
        self,
        input_convert_rocrate_collection_format,
        **kwargs
    ):
        """Convert Rocrate Collection Format  # noqa: E501

        convert_rocrate_collection_format Given a list of rocrate items will return a list of equal size with items in the same order. Each item represents a possible successful conversion into a collection format object. Each item includes an error field True/False for whether the conversion succeeds, a collection_format if it does and an error_message if it doesn't.  This method is designed to assist database migrations from the admin tools by providing the means to generate up to date collection format representations against the current schema. This can be used in conjunction with imports/exports to perform a quick database update.  Arguments ---------- rocrate_input_list : InputConvertRocrateCollectionFormat     The list of rocrate inputs  Returns -------  : ResponseConvertRocrateCollectionFormat     The list of possible collection format outputs  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post(input_convert_rocrate_collection_format, async_req=True)
        >>> result = thread.get()

        Args:
            input_convert_rocrate_collection_format (InputConvertRocrateCollectionFormat):

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
            ResponseConvertRocrateCollectionFormat
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
        kwargs['input_convert_rocrate_collection_format'] = \
            input_convert_rocrate_collection_format
        return self.convert_rocrate_collection_format_admin_registry_convert_rocrate_collection_format_post_endpoint.call_with_http_info(**kwargs)

    def export_registry_parsed_admin_registry_export_parsed_get(
        self,
        **kwargs
    ):
        """Export Registry Parsed  # noqa: E501

        export_registry_parsed Returns all the registry items parsed into the current RegistryItem format.  Returns -------  : RegistryParsedExport     The export object which has a list of entries.  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_registry_parsed_admin_registry_export_parsed_get(async_req=True)
        >>> result = thread.get()


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
            RegistryParsedExport
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
        return self.export_registry_parsed_admin_registry_export_parsed_get_endpoint.call_with_http_info(**kwargs)

    def export_registry_unparsed_admin_registry_export_unparsed_get(
        self,
        **kwargs
    ):
        """Export Registry Unparsed  # noqa: E501

        export_registry_unparsed Returns all the registry items without first parsing them as RegistryItems. This method is useful for a situation in which the items in the registry are no longer valid under the current RegistryItem model. You can use this method to dump the db, then modify it offline to be valid, then upload it using the parsed import endpoint to validate that the new entries are valid and are updating old entries as desired.  Returns -------  : RegistryUnparsedExport     The list of unparsed objects in Dict[str,Any] format.  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_registry_unparsed_admin_registry_export_unparsed_get(async_req=True)
        >>> result = thread.get()


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
            RegistryUnparsedExport
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
        return self.export_registry_unparsed_admin_registry_export_unparsed_get_endpoint.call_with_http_info(**kwargs)

    def import_registry_parsed_admin_registry_import_parsed_post(
        self,
        registry_parsed_import,
        **kwargs
    ):
        """Import Registry Parsed  # noqa: E501

        import_registry_parsed Given a list of registry items (parsed as valid before being accepted at this endpoint) this method will update the current registry, according to the rules you set in the other options, to match your import. This method is much safer than the unparsed method as it only allows valid RegistryItems in. However there could be situations where you want to preemptively update the registry before the API is updated to remove down time after update. See the options in ImportResponse, these are critical controls.  Arguments ---------- registry_import : RegistryParsedImport     The registry import object which contains configuration     options and the list of items. protected_roles : ProtectedRole, optional     _description_, by default Depends( admin_user_protected_role_dependency)  Returns -------  : ImportResponse     The response, which includes status info, statistics and     other items.  Raises ------ HTTPException     500 error if write failure occurs HTTPException     500 error if delete failure occurs  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_registry_parsed_admin_registry_import_parsed_post(registry_parsed_import, async_req=True)
        >>> result = thread.get()

        Args:
            registry_parsed_import (RegistryParsedImport):

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
            ImportResponse
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
        kwargs['registry_parsed_import'] = \
            registry_parsed_import
        return self.import_registry_parsed_admin_registry_import_parsed_post_endpoint.call_with_http_info(**kwargs)

    def import_registry_unparsed_admin_registry_import_unparsed_post(
        self,
        registry_unparsed_import,
        **kwargs
    ):
        """Import Registry Unparsed  # noqa: E501

        import_registry_unparsed Given a list of unparsed - unvalidated -registry items this method will update the current registry, according to the rules you set in the other options, to match your import. This method is much less safe vs the unparsed method as it allows any valid dynamodb record as RegistryItems. However there could be situations where you want to pre-emptively update the registry before the API is updated to remove down time after update. See the options in ImportResponse, these are critical controls.  Arguments ---------- registry_import : RegistryParsedImport     The registry import object which contains configuration     options and the list of items. protected_roles : ProtectedRole, optional     _description_, by default Depends( admin_user_protected_role_dependency)  Returns -------  : ImportResponse     The response, which includes status info, statistics and     other items.  Raises ------ HTTPException     500 error if write failure occurs HTTPException     500 error if delete failure occurs  See Also (optional) --------  Examples (optional) --------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_registry_unparsed_admin_registry_import_unparsed_post(registry_unparsed_import, async_req=True)
        >>> result = thread.get()

        Args:
            registry_unparsed_import (RegistryUnparsedImport):

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
            ImportResponse
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
        kwargs['registry_unparsed_import'] = \
            registry_unparsed_import
        return self.import_registry_unparsed_admin_registry_import_unparsed_post_endpoint.call_with_http_info(**kwargs)
