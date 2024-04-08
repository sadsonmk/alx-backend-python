#!/usr/bin/env python3
"""This is a module which implements tests for client.GithubOrgClient class"""

import unittest
from unittest import (Mock, patch, MagicMock)
from parameterized import parameterized
from typing import (
    List,
    Dict,
)
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """This class implements tests for test_org method"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
        ])
    @patch("client.get_json",)
    def test_org(self, org: str, result: Dict, func: MagicMock) -> None:
        """the method that tests the org function"""
        func.return_value = MagicMock(return_value=result)
        org_client_obj = GithubOrgClient(org)
        self.assertEqual(org_client_obj.org(), result)
        func.assert_called_once_with(f"https://api.github.com/orgs/{org}")


if __name__ == '__main__':
    unittest.main()
