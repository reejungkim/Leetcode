#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:28:24 2021

@author: reejungkim
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        sentence = ''
        for i in range(len(s)-1, -1, -1):
            sentence += s[i] +' '
        return sentence.strip()