# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:30:30 2024

@author: Hi
"""
import math
def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh') 
    tinh = kwargs.get('tinh') 
    if hinh == 'vuong':
        canh = args[0]
        if tinh == "cv": #Chu vi hình vuông
            return 4*canh 
        elif tinh == 'dt': # Diện tích hình vuông
            return canh*canh
    elif hinh == 'chu_nhat':
        dai = args[0]
        rong = args[1]
        if tinh == 'cv': #Chu vi HCN
            return 2*(dai + rong)
        elif tinh == 'dt': #Diện tích HCN
            return dai*rong
    elif hinh == 'tron':
        ban_kinh = args[0]
        if tinh == 'cv': #Chu vi hình tròn
            return 2*math.pi*ban_kinh
        elif tinh == 'dt': #Dien tich hinh tròn
            return math.pi*(ban_kinh)**2
    else: 
        print("Hình không hợp lệ")
# Gọi hàm theo đề bài 
print(tinh(10, hinh='vuong', tinh='cv'))
print(tinh(50, hinh='vuong', tinh='dt'))
print(tinh(18, hinh='tron', tinh='cv'))
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))
        
            
        