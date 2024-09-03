# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:48:23 2024

@author: Hi
"""
def ktgt(): 
    gia_tri = float(input("Nhập giá trị: "))
    if -89 <= gia_tri <= 90: 
        return gia_tri 
    else:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
        return ktgt()
gia_tri_hop_le = ktgt()
print(f"Gia tri hop le: {gia_tri_hop_le}")