# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:01:58 2024

@author: Hi
"""

N = int(input("Nhập vào số nguyên dương N: "))
while N <= 0:
    print("Số bạn vừa nhập không phải là số nguyên dương. Vui lòng nhập lại")
    N = int(input("Hãy nhập một số nguyên dương: "))
else: 
    print(f"Các ước số của {N} là:")
    for i in range(1, N + 1): 
        if N % i == 0: 
            print(i)
    