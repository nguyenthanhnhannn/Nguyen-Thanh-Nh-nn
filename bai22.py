# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:11:46 2024

@author: Hi
"""
a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số nguyên b: "))
if a == 0: 
    if b == 0: 
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
print("Phương trình có nghiệm x:", x)