#!/usr/bin/env python3
"""contains a TestAccessNestedMap class that inherits from unittest.TestCase"""

import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Implements the TestAccessNestedMap.test_access_nested_map method
        to test that the method returns what it is supposed to
    """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",)),
                ({"a": {"b": 2}}, ("a",)),
                ({"a": {"b": 2}}, ("a", "b")),
                ]
            )
    def test_access_nested_map(self, nested_map, path, expected):
        """tests the nested map"""
        self.assertEqual(
           access_nested_map(access_nested_map(nested_map, path), expected))


if __name__ == "__main__":
    unittest.main()
