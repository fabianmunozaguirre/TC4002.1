# -*- coding: utf-8 -*-
"""
Given the math.ceil function and the the filecmp.cmp function
Define a set of test cases that exercise the function (Remember Right BICEP)

"""
import unittest
import math

class TestStringMethods(unittest.TestCase): 
    def test_math_ceil(self):
        result = math.ceil(1.2)
        self.assertEqual(result, 2.0)

if __name__ == '__main__':
    unittest.main()
