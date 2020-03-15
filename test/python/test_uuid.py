#!/usr/bin/env python3

import unittest
import sys

sys.path.append('/bin')

import uuid

class TestUuid(unittest.TestCase):

    def test_random_uuid(self):
        self.assertEqual("a", randomUuid())

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
