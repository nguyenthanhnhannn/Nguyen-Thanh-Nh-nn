# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:38:50 2024

@author: Hi
"""
# a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
    a, b = b, a  # Đổi chỗ a và b
if a > c:
    a, c = c, a  # Đổi chỗ a và c
if b > c:
    b, c = c, b  # Đổi chỗ b và c
print("Thứ tự tăng dần: ", a, b, c)

# b 
N = int(input("Nhập số nguyên N: "))
ket_qua = int(''.join(sorted(str(N)))) # join ghép kí tự trong danh sách thành chuỗi mới
                                        # sorted sắp xếp theo kí tự tăng dần
print("Số có các chữ số theo thứ tự tăng dần là:", ket_qua)
