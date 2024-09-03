# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:29:32 2024

@author: Hi
"""

n = int(input("Nhập số nguyên dương lẻ: "))
while n <= 0 or n % 2 == 0:
    print("n phải là số lẻ và lớn hơn 0")
    n = int(input("Hãy nhập lại số nguyên dương lẻ: "))
else: 
    s = 1 
    for i in range(1, n + 1): 
        s = s * i
    print("Kết quả của S là: ", s)
   