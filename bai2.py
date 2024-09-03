# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:05:25 2024

@author: Hi
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
tong = a + b
hieu = a - b 
tích = a * b 
thuong = a / b 
print("Tổng của a và b là:" , tong)
print("Hiệu của a và b là:" , hieu)
print("Tích của a và b là:" , tích)
print("Thương của a và b là:" , thuong)
print("Thương làm tròn 2 chữ số:" ,round(thuong,2))
print("Thương làm tròn 3 chữ số:" ,round(thuong,3))