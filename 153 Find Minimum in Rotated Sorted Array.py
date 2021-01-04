#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:31:43 2021

@author: reejungkim
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        minimum = nums[0]
        for val in nums:
            if val < minimum:
                minimum = val
        return minimum