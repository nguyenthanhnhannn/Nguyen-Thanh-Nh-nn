# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:22:43 2024

@author: Hi
"""

n = str(input("hãy nhập vào giờ/phút/giây: "))
h,m,s = map(int, n.split('/'))
if h >= 0 and m >= 0 and s >= 0:
    giay = (h * 3600) + (m * 60) + s 
    print("Số giây đổi được là: ", giay)
