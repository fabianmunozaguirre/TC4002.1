# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:06:21 2021

@author: fabmunoz
"""
import unittest

file_a = "C:\\Users\\fabmunoz\\Documents\\Personal - Maestria\\TC4002.1\\Lab 3\\file_a.txt"
file_b = "C:\\Users\\fabmunoz\\Documents\\Personal - Maestria\\TC4002.1\\Lab 3\\file_b.txt"

class TestFileCmpMethods(unittest.TestCase):
    def test_filecpm_cmp(self):
        result = filecmp.cmp(file_a, file_b) 
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()