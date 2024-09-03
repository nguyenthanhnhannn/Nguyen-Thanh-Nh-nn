# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:01:34 2024

@author: Hi
"""

n = int( input("nhập vào 1 số chắn có giá trị âm: "))
def kt_sc_a(n) :
    if n < 0 and n % 2 == 0 : #Kiểm tra nếu số là số chẵn và có giá trị âm
        return True # True nếu số là số chẵn và có giá trị âm
    else :
        return False # Ngược lại là false
print(kt_sc_a(n))