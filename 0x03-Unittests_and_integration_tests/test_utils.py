#!/usr/bin/env python3
"""contains a TestAccessNestedMap class that inherits from unittest.TestCase"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (access_nested_map, get_json)
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Implements the TestAccessNestedMap.test_access_nested_map method
        to test that the method returns what it is supposed to
    """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2),
                ]
            )
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, ep):
        """tests the nested map"""
        self.assertEqual(access_nested_map(nested_map, path), ep)

    @parameterized.expand(
            [
                ({}, ("a",), KeyError),
                ({"a", 1}, ("a", "b"), KeyError),
                ]
            )
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """tests for an exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """This class tests the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """Tests the get_json for a certain payload from a given url"""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as requested:
            self.assertEqual(get_json(test_url), test_payload)
            requested.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """implements the memoize tests"""
    def test_memoize(self):
        """this tests the memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                'a_method',
                return_value=lambda: 42,
                ) as result:
            obj = TestClass()
            self.assertEqual(obj.a_property(), 42)
            self.assertEqual(obj.a_property(), 42)
            result.assert_called_once()


if __name__ == "__main__":
    unittest.main()
