"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.access_check_api import AccessCheckApi  # noqa: E501


class TestAccessCheckApi(unittest.TestCase):
    """AccessCheckApi unit test stubs"""

    def setUp(self):
        self.api = AccessCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_admin_access_check_access_check_admin_access_get(self):
        """Test case for check_admin_access_check_access_check_admin_access_get

        Check Admin Access  # noqa: E501
        """
        pass

    def test_check_general_access_check_access_check_general_access_get(self):
        """Test case for check_general_access_check_access_check_general_access_get

        Check General Access  # noqa: E501
        """
        pass

    def test_check_read_access_check_access_check_read_access_get(self):
        """Test case for check_read_access_check_access_check_read_access_get

        Check Read Access  # noqa: E501
        """
        pass

    def test_check_write_access_check_access_check_write_access_get(self):
        """Test case for check_write_access_check_access_check_write_access_get

        Check Write Access  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
