# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:50:54 2024

@author: Hi
"""

n = int(input("Nhập số nguyên dương n: "))
while n < 0: 
    print("Số bạn vừa nhập không phải là số nguyên dương")
    n = int(input(" Hãy nhập lại số nguyên dương n: "))
else: 
    s = 0 
    for i in range(1,n+1): 
        s = s + i**2
    print("Tổng của S là: ", s)