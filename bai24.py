# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:17:24 2024

@author: Hi
"""

a = int(input("Nhập vào giờ: "))
b = int(input("Nhập vào phút: "))
c = int(input("Nhập vào giây: "))
if 0 <= a < 24 and 0 <= b < 60 and 0 <= c < 60:
    print("Giờ, phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")