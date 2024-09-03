# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:18:36 2024

@author: Hi
"""

def tim_nghiem():
    nghiem = []
    min = float('inf')
    
    for x in range(1, 490):
        for y in range(1, 140):
            z = (979 - 2*x - 7*y) / 9
            if z.is_integer() and z > 0:
                z = int(z)
                if x + y + z < min:
                    min = x + y + z
                    nghiem = [(x, y, z)]
                elif x + y + z == min:
                    nghiem.append((x, y, z))
    
    return nghiem
nghiem = tim_nghiem()
for nghiem in nghiem:
    print(f"Các nghiệm có tổng x + y + z nhỏ nhất là: {nghiem}")