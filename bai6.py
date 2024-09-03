# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:41:33 2024

@author: Hi
"""

n = int(input("Nhập năm sinh của bạn: "))
if 0 <= n < 2024: 
    t = 2024 - n 
    print(f"Bạn sinh năm {n} vậy bạn {t} tuổi") 
elif n == 2024:
    print("Bạn chưa được 1 tuổi ")
else: 
    print("Năm sinh bạn nhập không hợp lệ: ")
    
    