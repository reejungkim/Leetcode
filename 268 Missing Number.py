#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:31:27 2021

@author: reejungkim
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        tot_exp = (n+1)*n//2
        return tot_exp - tot