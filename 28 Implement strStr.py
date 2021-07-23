#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:15:59 2021

@author: reejungkim
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1