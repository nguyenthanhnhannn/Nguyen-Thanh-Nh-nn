# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:07:28 2024

@author: Hi
"""

a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
while a < 0 or b < 0 or c < 0: 
    print("Số bạn vừa nhập không phải là số nguyên dương")
    a = int(input("Nhập cạnh thứ nhất: "))
    b = int(input("Nhập cạnh thứ hai: "))
    c = int(input("Nhập cạnh thứ ba: "))
else: 
    if (a+b)>c and (b+c>a) and (c+a>b): 
        print("Đây là 3 cạnh của 1 tam giác") 
        if a == b == c:
         print("Tam giác đều")
        elif a == b or b == c or a == c:
         print("Tam giác cân")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
         print("Tam giác vuông")
        else: 
         print("Tam giác thường") 
    else: 
        print("Đây không phải là 3 cạnh của tam giác")
    
      

    