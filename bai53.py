# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:28:28 2024

@author: Hi
"""

import math

# a) S = 1 + 2 + 3 + ...... + n
def a(n):
    return sum(range(1, n + 1))

# b) S = 1^2 + 2^2 + 3^2 + ...... + n^2
def b(n):
    return sum(i ** 2 for i in range(1, n + 1))

# c) S = 1 + 1/2 + 1/3 + ...... + 1/n
def c(n):
    return sum(1 / i for i in range(1, n + 1))

# d) S = 1! + 2! + 3! + ...... + n!
def d(n):
    return sum(math.factorial(i) for i in range(1, n + 1))

# e) S = 1 * 2 * 3 * ...... * n
def e(n):
    return math.prod(range(1, n + 1))

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Sử dụng các phương thức và in kết quả
print(f"S = 1 + 2 + 3 + ...... + {n} là: {a(n)}")
print(f"S = 1^2 + 2^2 + 3^2 + ...... + {n}^2 là: {b(n)}")
print(f"S = 1 + 1/2 + 1/3 + ...... + 1/{n} là: {c(n)}")
print(f"S = 1! + 2! + 3! + ...... + {n}! là: {d(n)}")
print(f"S = 1 * 2 * 3 * ...... * {n} là: {e(n)}")