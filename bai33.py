# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:31:14 2024

@author: Hi
"""
import math
n = int(input("Nhập số nguyên dương n: "))
while n < 0: 
    print("Số bạn vừa nhập không phải là số nguyên dương")
    n = int(input("Hãy nhập lại số nguyên dương n: "))
else: 
    if n > 0: 
        x = int(math.sqrt(n))
    if  x*x == n:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
    