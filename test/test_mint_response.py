"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_data_api
from rrap_mds_is_data_api.model.s3_location import S3Location
from rrap_mds_is_data_api.model.status import Status
globals()['S3Location'] = S3Location
globals()['Status'] = Status
from rrap_mds_is_data_api.model.mint_response import MintResponse


class TestMintResponse(unittest.TestCase):
    """MintResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMintResponse(self):
        """Test MintResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MintResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
