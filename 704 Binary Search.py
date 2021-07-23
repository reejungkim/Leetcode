#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:35:37 2021

@author: reejungkim
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
        except:
            index = -1
        return index