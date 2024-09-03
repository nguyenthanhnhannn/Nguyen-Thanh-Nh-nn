# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:32:42 2024

@author: Hi
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tu1 = a + b 
mau1 = a**(1/3) + b**(1/3)
tu2 = (a*b)**(1/3)
tu3 = (a**(1/3) - b**(1/3))**2
ket_qua = (tu1/mau1 - tu2) / tu3
print("Kết quả biểu thức là: ", ket_qua)