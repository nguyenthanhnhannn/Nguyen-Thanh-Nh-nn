# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:58:52 2024

@author: Hi
"""

n = int(input("hãy nhập vào số nguyên n dương: "))
s = 0
while n < 0 :
    n = int(input("hãy nhập lại số nguyên n dương: "))
else: 
    for i in range(1, n + 1):
        s = s + ((2 * i - 1) / (2 * i))
    print("Tổng của S là: ", s)