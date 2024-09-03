# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:15:49 2024

@author: Hi
"""
n = int(input("hãy nhập vào số nguyên n dương: "))
s = 0
while n < 0 :
    n = int(input("hãy nhập lại số nguyên n dương: "))
else: 
    s = 0
    for i in range(n + 1):
        s = s + (1 / ((2 * i )+ 1))
    print("Tổng của S là: ", s)