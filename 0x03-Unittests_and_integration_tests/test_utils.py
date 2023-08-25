#!/usr/bin/python3
'''Module for parameterized testing of utils.access_nested_map'''
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''Class to to test access_nested_map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, x, y, expected):
        '''test access_nested_map'''
        result = access_nested_map(x, y)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, x, y, exception):
        '''test access_nested_map_exception'''
        with self.assertRaises(exception):
            access_nested_map(x, y)


class TestGetJson(unittest.TestCase):
    '''Class to test get_json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''get_json function'''
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Class to test memoize'''

    def test_memoize(self):
        '''test_memoize function'''
        class TestClass:
            '''Test Class'''

            def a_method(self):
                '''test property'''
                return 42

            @memoize
            def a_property(self):
                '''test property'''
                return self.a_method()
        method = TestClass()
        with patch.object(method, 'a_method') as mock_method:
            result = method.a_property()
            result1 = method.a_property()
            mock_method.assert_called_once()
            self.assertEqual(result, result1)


if __name__ == '__main__':
    unittest.main()
