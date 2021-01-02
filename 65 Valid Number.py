#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 00:08:06 2021

@author: reejungkim
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False