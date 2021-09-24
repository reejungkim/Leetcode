#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:58:20 2021

@author: reejungkim
"""
# 7.Reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            number= int(str(x)[::-1])
        elif x<0:
            number= int(str(x*-1)[::-1])*-1
            
        if number <= (-2**31) or number>= (2**31):
            return 0
        else :
            return number
        
        