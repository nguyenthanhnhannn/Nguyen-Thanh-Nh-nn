# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:34:52 2024

@author: Hi
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
if 10 <= N <= 99: 
    x = N // 10
    y = N % 10 
    z = x + y 
print(f"tổng các chữ số của {N} là {x} + {y} = {z} ")