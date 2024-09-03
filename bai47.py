# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:58:19 2024

@author: Hi
"""

def tim_nghiem():
    nghiem = []
    max = 0
    for x in range(1, 490):
        for y in range(1, 140):
            z = (979 - 2*x - 7*y) / 9
            if z.is_integer() and z > 0:
                z = int(z)
                if x + y + z > max:
                    max = x + y + z
                    nghiem = [(x, y, z)]
                elif x + y + z == max:
                    nghiem.append((x, y, z))
    
    return nghiem
nghiem = tim_nghiem()
for nghiem in nghiem:
    print(f"Các nghiệm có tổng x + y + z lớn nhất là: {nghiem}")