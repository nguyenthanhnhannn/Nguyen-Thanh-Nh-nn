# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:03:18 2024

@author: Hi
"""

xe = input(" nhập vào số xe cua ban ( 4 số): ")
a = int(xe[0])
b = int(xe[1])
c = int(xe[2])
d = int(xe[3])
if len(xe) == 4 :
    n = (a + b + c + d) % 10
    print(f"số nút của xe bạn là: {n}")
else:
    print("biển số xe sai")

        
    