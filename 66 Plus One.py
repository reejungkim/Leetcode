#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:48:47 2021

@author: reejungkim
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_string = ''
        solution = []
        for digit in digits:
            digits_string += str(digit)
        x = str(int(digits_string)+1)
        x = x.rjust(len(digits_string), '0')
        for val in x:
            solution.append(val)
        return solution