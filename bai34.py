# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:37:28 2024

@author: Hi
"""

n = int(input("nhập vào số nguyên dương: "))
while n < 0:
    print("Số bạn vừa nhập không phải số nguyên dương")
    n = int(input("Hãy nhập lại số nguyên dương: "))
else: 
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    if is_prime(n): # Hàm is_prime(n) ktra xem n là số nguyên tố hay không
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")