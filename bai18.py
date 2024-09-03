# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:02:49 2024

@author: Hi
"""

a = str(input("nhập giờ thứ nhất (giờ,phút,giây): "))
b = str(input("nhập giờ thứ hai (giờ,phút,giây): "))
h1, m1, s1 = map(int, a.split(','))
h2, m2, s2 = map(int, b.split(','))
giay1 = h1 * 3600 + m1 * 60 + s1
giay2 = h2 * 3600 + m2 * 60 + s2
if giay1 > 0 and giay2 > 0:
    t = giay1 + giay2
    if giay1 > giay2 :
        hh = giay1 - giay2
    else :
        hh = giay2 - giay1
ht = t // 3600 
mt = t // 60 - ht * 60
st = t - ht * 3600 - mt * 60 
h = hh // 3600 
m = hh // 60 - h * 60
s = hh - h * 3600 - m * 60 
print(f"kết quả cộng của 2 giờ là: {ht}:{mt}:{st}")
print(f"kết quả trừ của 2 giờ là: {h}:{m}:{s}")