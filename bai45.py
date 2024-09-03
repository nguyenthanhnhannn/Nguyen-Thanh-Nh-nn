# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:11:47 2024

@author: Hi
"""

def kq(x,n):
    s = 0 
    for i in range(1, n+1):
        tu = x**i
        mau = sum(range(1, i+1))
        s = s + (tu / mau)
    return s 

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
ket_qua = kq(x,n) 
print("Kết quả là: ", ket_qua)
        