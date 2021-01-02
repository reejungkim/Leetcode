#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 00:14:59 2021

@author: reejungkim
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = int(a,2) + int(b,2)
        return str(bin(total)[2:])
        