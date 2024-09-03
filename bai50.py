# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:40:21 2024

@author: Hi
"""
n = int(input("Nhập một số: "))
def kiem_tra_so(n): 
    if n < 0 and n % 2 != 0:
        return -1 
    elif n > 0 and n % 2 == 0:
        return 1
    else:
        return 0
print(kiem_tra_so(n))