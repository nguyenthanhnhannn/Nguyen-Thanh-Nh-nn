# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:47:59 2024

@author: Hi
"""

def tim_nghiem():
    nghiem = []
    for x in range(1, 490):  # x phải lớn hơn 0 và nhỏ hơn 490 vì 2*490 = 980 > 979
        for y in range(1, 140):  # y phải lớn hơn 0 và nhỏ hơn 140 vì 7*140 = 980 > 979
            for z in range(1, 109):  # z phải lớn hơn 0 và nhỏ hơn 109 vì 9*109 = 981 > 979
                if 2*x + 7*y + 9*z == 979:
                    nghiem.append((x, y, z))  # thêm bộ nghiệm vào danh sách
    return nghiem

# Gọi hàm và in kết quả
bo_nghiem = tim_nghiem()
for x, y, z in bo_nghiem:
    print(f"Bộ nghiệm: x = {x}, y = {y}, z = {z}")