# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:41:15 2024

@author: Hi
"""

qd = float(input("nhập vào quảng đường cần đi km ( quảng đường cần đi phải là số dương): "))
while qd < 0 :
    print("hãy nhập lại")
    qd = float(input("nhập vào quảng đường cần đi km ( quảng đường cần đi phải là số dương): "))
else :
    if 0 <= qd <= 1 :
        t = 15000
    elif  qd < 2 :
        t =  qd * 15000
    elif 2 <= qd < 6 :
        t = 15000 + (qd - 1) * 13500
    elif 6 <= qd :
        t = 15000 + (4 * 13500) + (qd - 5) * 11000
    elif qd > 120 :
        t = t - (t *0.1)
print(f"số tiền cước taxi cần trả cho {qd}km là : {t} đ")