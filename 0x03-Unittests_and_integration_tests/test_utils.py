#!/usr/bin/env python3
"""contains a TestAccessNestedMap class that inherits from unittest.TestCase"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
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


if __name__ == "__main__":
    unittest.main()
