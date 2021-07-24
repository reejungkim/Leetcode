#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:51:04 2021

@author: reejungkim
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move =='R':
                x +=1
            elif move =='L':
                x -=1
            elif move =='U':
                y +=1
            elif move == 'D':
                y -=1
        return x==y==0