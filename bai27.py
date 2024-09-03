# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:21:07 2024

@author: Hi
"""

import math
loai_hinh = input("Nhập loại hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")
if loai_hinh == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    chu_vi = 4*canh
    dien_tich = canh*canh
    print("Chu vi hình vuông là: ", chu_vi)
    print("Diện tích hình vuông là: ", dien_tich)
elif loai_hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    chu_vi = 2* (chieu_dai + chieu_rong)
    dien_tich = chieu_dai*chieu_rong
    print("Chu vi hình chữ nhật là: ", chu_vi)
    print("Diện tích hình chữ nhật là: ", dien_tich)
elif loai_hinh == 't': 
    r = float(input("Nhập bán kính đường tròn: ")) 
    chu_vi = 2*math.pi*r
    dien_tich = math.pi*r*r
    print("Chu vi hình tròn là: ", chu_vi) 
    print("Diện tích hình tròn là: ", dien_tich) 
else: 
    print("Loại hình không hợp lệ")
    
        
    
