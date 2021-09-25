#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:51:41 2021

@author: reejungkim
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n-1) == 0) and n != 0
    
    
    



"""
Explanation: 
    every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index). So when subtracting 1 from it, that bit flips to 0 and all preceding bits flip to 1. That makes these 2 numbers the inverse of each other so when AND-ing them, we will get 0 as the result.
"""