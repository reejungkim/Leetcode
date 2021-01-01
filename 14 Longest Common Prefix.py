#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:19:40 2021

@author: reejungkim
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""

        for x in zip(*strs):   
            if len(set(x)) == 1:
                prefix += str(x[0])
            else:
                break
        return prefix 

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         StopIteration=False
#         if len(strs)==0:
#             return ""
#         index_limit = len(min(strs, key=len))
#         i = 0

#         while i < (index_limit):
#             prefix = strs[0][i] #d
#             for word in strs: 
#                 if prefix != word[i]:
#                     StopIteration = True
#                     break
#             if StopIteration == True:
#                 break
#             i += 1
               
#         return strs[0][:i]
            