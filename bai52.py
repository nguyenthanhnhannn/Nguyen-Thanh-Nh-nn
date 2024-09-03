# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:00:41 2024

@author: Hi
"""

import math

def can_bac_x(n, x):
    return n ** (1/x)

def so_dao(n):
    return int(str(n)[::-1])

def la_so_chinh_phuong(n):
    return int(math.sqrt(n))**2 == n

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tich_cac_chu_so_le(n):
    tich = 1
    le = False
    while n > 0:
        s = n % 10
        if s % 2 != 0:
            tich = tich * s
            le = True
        n //= 10
    return tich if le else 0

def tong_cac_so_nguyen_to_nho_hon(n):
    tong = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong = tong + i
    return tong

def tong_cac_so_chinh_phuong_nho_hon(n):
    tong = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        tong = tong + (i * i)
    return tong

def tong_cac_uoc_so_duong(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong = tong + i
    return tong

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
print(f"Căn bậc {x} của {n} là: {can_bac_x(n, x)}")
print(f"Số đảo của {n} là: {so_dao(n)}")
print(f"{n} có phải là số chính phương không? {la_so_chinh_phuong(n)}")
print(f"{n} có phải là số nguyên tố không? {la_so_nguyen_to(n)}")
print(f"Tích các chữ số lẻ của {n} là: {tich_cac_chu_so_le(n)}")
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_cac_so_nguyen_to_nho_hon(n)}")
print(f"Tổng các số chính phương nhỏ hơn {n} là: {tong_cac_so_chinh_phuong_nho_hon(n)}")
print(f"Tổng các ước số dương của {n} là: {tong_cac_uoc_so_duong(n)}")