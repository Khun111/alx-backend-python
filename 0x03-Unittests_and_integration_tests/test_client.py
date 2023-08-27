#!/usr/bin/env python3
'''Module for test_client'''
import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''Test GithubOrgClient Class'''
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, org_name, payload, mock_get):
        '''Function to test org'''
        mock_get.return_value = payload
        result = GithubOrgClient.org()

        self.assertEqual(result, payload)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        '''Function to test public_repos_url '''
        with mock.patch(
            'client.GithubOrgClient._public_repos_url'
        ) as mock_org:
            mock_org.return_value = {"payload": True}
            result = GithubOrgClient._public_repos_url()
            self.assertEqual(result, {"payload": True})

    def test_public_repos(self):
        '''Function to test public_repos'''
        with mock.patch(
            'client.GithubOrgClient.public_repos'
        ) as mock_org:
            mock_org.return_value = ['u', 'will', 'always', 'be', 'my', 'fan']
            result = GithubOrgClient.public_repos()
            self.assertEqual(
                result, ['u', 'will', 'always', 'be', 'my', 'fan'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, licenses, license_key, expected):
        '''Test for has_license'''
        result = GithubOrgClient.has_license(licenses, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration tests for punlic repos'''
    @classmethod
    def setUpClass(cls):
        '''Setup class method'''
        payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def side_effect(url):
            '''Side effect function'''
            if url in payloads:
                return MagicMock(**{'json.return_value': payloads[url]})
        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''Class for tearDown'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test repos without license'''
        git_client = GithubOrgClient("google")
        result = git_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        '''Test repos with license'''
        git_client = GithubOrgClient("google")
        result = git_client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
