#!/usr/bin/env python3
"""
test file
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test class"""

    @parameterized.expand([
        ({"a": 1}, 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Implement the
        TestAccessNestedMap.test_access_nested_map method
        """
        result = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(result, expected)
