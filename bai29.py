# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:21:07 2024

@author: Hi
"""

n = int(input("Nhập số nguyên dương N: "))
s = 0
while n < 0:
    print("Số bạn nhập không phải là số nguyên dương")
    n = int(input('Hãy nhập lại số nguyên dương N: '))
else: 
    while n > 0:
        s = s + ( n % 10 )
        n = n // 10
print("Tổng các chữ số nguyên dương N là: ", s)

