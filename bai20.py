# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:08:39 2024

@author: Hi
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
lon = a
if b > lon:
   lon = b
if c > lon:
   lon = c
print("Số lớn nhất là:", lon)