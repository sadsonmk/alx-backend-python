#!/usr/bin/env python3
"""This is a module which implements tests for client.GithubOrgClient class"""

import unittest
from unittest import (Mock, patch, MagicMock, PropertyMock)
from parameterized import parameterized, parameterized_class
from typing import (
    List,
    Dict,
)
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """This class implements tests for test_org method"""

    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch("client.get_json",)
    def test_org(self, org: str, result: Dict, func: MagicMock) -> None:
        """the method that tests the org function"""
        func.return_value = MagicMock(return_value=result)
        org_client_obj = GithubOrgClient(org)
        self.assertEqual(org_client_obj.org(), result)
        func.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Implement the test_public_repos_url method to unit-test
            GithubOrgClient._public_repos_url
        """
        with patch.object(
                GithubOrgClient.org,
                "org",
                ) as mock_obj:
            res = {"repos_url": "https://api.github.com/orgs/test-org/repos"}
            exp_url = res['repos_url']
            mock_obj.return_value = res

            client = GithubOrgClient("test-org")

            public_repos_url = client._public_repos_url()
            self.assertEqual(public_repos_url, exp_url)

    @patch("client.get_json")
    def test_public_repos(self):
        """mocks get_json and _public_repos_url"""
        with patch.object(GithubOrgClient, "get_json") as mock_get_json, \
                patch.object(GithubOrgClient, "_public_repos_url") as mock_url:

            exp_url = "https://api.github.com/test-org/repos"
            mkd_repo = [{"name": "my_repo1"}, {"name": "my_repo2"}]
            mock_url.return_value = exp_url
            mock_get_json.return_value = mkd_repo

            client = GithubOrgClient("test-org")
            public_repos = client.public_repos()

            self.assertEqual(public_repos, [rep["name"] for rep in mkd_repo])
            mock_get_json.assert_called_once_with(exp_url)
            mock_url.assert_called_once_with()

    @parameterized.expand(
            [
                ({"license": {"key": "my_license"}}, "my_license", True),
                ({"license": {"key": "other_license"}}, "my_license", False),
                ]
            )
    def test_has_license(self, repo, license_key, exp):
        """implements test_has_license to
            unit-test GithubOrgClient.has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, exp)


@parameterized_class(
        [
            {
                'org_payload': TEST_PAYLOAD[0][0],
                'repos_payload': TEST_PAYLOAD[0][1],
                'expected_repos': TEST_PAYLOAD[0][2],
                'apache2_repos': TEST_PAYLOAD[0][3],
                                }
            ]
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """implements testing using a parameterized class"""
    @classmethod
    def setUpClass(cls):
        """sets up basic requirements before running tests"""
        return_payload = {
                "https://api.github.com/test-org": cls.org_payload,
                "https://api.github.com/test-org/repos": cls.repos_payload,
                }

        def get_payload(url):
            """gets payload based on return_payload"""
            if url in return_payload:
                return Mock(**{'json.return_value': return_payload[url]})
            return requests.HTTPError
        cls.get_patcher = patch("request.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Implements tests for the public_repos method"""
        self.assertEqual(
                GithubOrgClient("github").public_repos(),
                self.expected_repos,
                )

    def test_public_repos_with_license(self):
        """Implements tests for public_repos_with_license"""
        self.assertEqual(
                GithubOrgClient("github").public_repos(license="apache-2.0"),
                self.apache2_repos,
                )

    @classmethod
    def tearDownClass(cls):
        """teardown the tests"""
        cls.get_patcher.stop()
