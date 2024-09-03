# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:58:57 2024

@author: Hi
"""

n = int(input("Nhập vào một số chẵn dương: "))
while n <= 0 or n % 2 != 0: 
    print("n phải là số chẵn và lớn hơn 0.") 
    n = int(input("Hãy nhập vào một số chẵn dương: "))
else: 
     s = 0 
     for i in range(2, n + 1, 2): 
         s = s + i
     print("Tổng của S là: ", s)
     