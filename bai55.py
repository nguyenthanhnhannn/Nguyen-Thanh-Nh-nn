# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:21:56 2024

@author: Hi
"""

# Tạo hàm
def chu_vi(dai,rong): 
    return 2*(dai+rong)
def dien_tich(dai,rong):
    return dai*rong
def hinh_ve(dai,rong):
    for i in range(dai):
        for j in range(rong):
            print('*', end=' ')
        print()

# Nhập độ dài hai cạnh của hình chữ nhật
dai = int(input("Nhập chiều dài hình chữ nhật: "))
rong = int(input("Nhập chiều rộng hình chữ nhật: "))
# Tính chu vi và diện tích
chuvi = chu_vi(dai,rong)
dientich = dien_tich(dai,rong)
# In kết quả
print(f"Chu vi hình chữ nhật là: {chuvi}")
print(f"Diện tích hình chữ nhật là: {dientich}")

# Vẽ hình chữ nhật
print("Hình chữ nhật:")
hinh_ve(dai,rong)
