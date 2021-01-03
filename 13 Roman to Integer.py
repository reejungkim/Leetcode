#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:56:53 2021

@author: reejungkim
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = int(dict[s[-1]]) 
        solution = 0
        for i in range(len(s)-1, -1, -1):
            if number > dict[s[i]]:
                solution += (number - dict[s[i]] - number )
            else:
                solution += dict[s[i]]
            number = dict[s[i]]
        return solution
        