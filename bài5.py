# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:13:08 2024

@author: Hi
"""

s = input("nhập vào giờ, phút và giây theo định dạng hh:mm:ss: ")
h, m, s = map(int, s.split(':'))
if h >= 0 and m >= 0 and s >= 0:
    giay = (h * 3600) + (m * 60) + s 
    print("Số giây đổi được là: ", giay)

    
