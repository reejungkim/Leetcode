#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:21:59 2021

@author: reejungkim
"""

 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, number in enumerate(nums):
            arr = nums[:]
            if target-number in nums and i != nums.index(target-number):
                return [i, nums.index(target-number)]
        return []