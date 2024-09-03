# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:34:18 2024

@author: Hi
"""

time = input("Nhập thời gian theo định dạng ngày tháng năm: ")
a,b,c = map(int, time.split(' '))
if 1<=a<=31 and  1<=b<=12 and 1000<=c<=2024:
    print(f"{a}/{b}/{c}")
    print(f"{a}/{b}/{str(c)[-2:]}")
    print(f"{c}/{b}/{a}")
else:
    print("ngay thang nam khong hop le")
    
time = input("Nhập thời gian theo định dạng ngày/tháng/năm: ")
a,b,c = map(int, time.split('/'))
if 1<=a<=31 and  1<=b<=12 and 1000<=c<=2024:
    print(f"{a} {b} {c}")
    print(f"{a} {b} {str(c)[-2:]}")
    print(f"{c} {b} {a}")
else:
    print("ngay thang nam khong hop le")