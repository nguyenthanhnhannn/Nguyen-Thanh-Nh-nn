# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:25:56 2024

@author: Hi
"""

a = int(input("Nhập vào tháng: "))
b = int(input("Nhập vào năm: "))
if a == 2:
    if (b % 4 == 0 and b % 100 != 0) or (b % 400 == 0):
        ngay = 29
    else:
        ngay = 28
if a in [1,3,5,7,8,10,12] :
     ngay = 31 
elif a in [4,6,9,11] :
     ngay = 30 
print(f"Tháng {a} năm {b} có {ngay} ngày.")