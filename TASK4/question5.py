# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:13:12 2022

@author: Harshini
"""
# to print a pyramid of stars
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")

    for k in range (0,i+1):
        print("* ",end="")
    print("\r");          
