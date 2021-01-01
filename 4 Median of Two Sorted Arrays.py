#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:52:20 2021

@author: reejungkim
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n==1:
            median = merged[0]
        elif n%2 ==1:
            median = merged[n//2]
        else:
            median = (merged[n//2] + merged[n//2-1])/2
        
        return median