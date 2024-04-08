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
                ({}, ("a",), "'a'"),
                ({"a", 1}, ("a", "b"), "'b'"),
                ]
            )
    def test_access_nested_map_exception(self, nested_map, path, exp_excp):
        """tests for an exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), exp_excp)


if __name__ == "__main__":
    unittest.main()
