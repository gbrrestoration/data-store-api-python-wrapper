"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_data_api
from rrap_mds_is_data_api.model.collection_format import CollectionFormat
from rrap_mds_is_data_api.model.s3_location import S3Location
globals()['CollectionFormat'] = CollectionFormat
globals()['S3Location'] = S3Location
from rrap_mds_is_data_api.model.registry_item import RegistryItem


class TestRegistryItem(unittest.TestCase):
    """RegistryItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegistryItem(self):
        """Test RegistryItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RegistryItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
