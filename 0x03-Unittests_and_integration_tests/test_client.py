#!/usr/bin/env python3
'''Module for test_client'''
import unittest
from unittest import mock
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


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
        def test_has_license(licenses, license_key, expected):
            '''Test for has_license'''
            result = GithubOrgClient.has_license(licenses, license_key)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
