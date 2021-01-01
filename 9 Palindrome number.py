#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:09:55 2021

@author: reejungkim
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x)<=1:
            return True 
        for i in range(len(x)//2):
            if x[i] != x[len(x)-i-1] :
                return False
        return True
        