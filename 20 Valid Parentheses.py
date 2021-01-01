#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:11:21 2021

@author: reejungkim
"""

class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        dict = { "{":"}" , "[":"]", "(":")"}
        for val in s:
            if val in "{,[,(":
                arr.append(val)
            elif arr and dict[arr[-1]]==val:
                arr.pop()
            else:
                return False
        if len(arr)!=0:
            return False
        return True
        