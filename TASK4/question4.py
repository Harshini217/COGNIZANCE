# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:19:09 2022

@author: Harshini
"""

# Palindrome check
# considering we have only numeric values
num=int(input("ENTER A NUMBER TO CHECK IF IT IS PALINDROME OR NOT:"))
org=num
rev=0
rem=0
while(num > 0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if (org == rev):
# to return true if the given number is a palindrome!
    print("TRUE")
else:
# to return false if the given number is not a palindrome!
    print("FALSE")