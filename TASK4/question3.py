# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:10:21 2022

@author: Harshini
"""

from tabulate import tabulate
headers=[["ROLL NO", "NAME", "MARKS"]]
n = int(input("HOW MANY RECORDS DO YOU NEED IN TABLE:"))
for i in range (1,n+1):
    rollno=int(input("enter the roll no.: "))
    name=input("enter the name: ")
    marks= int(input("enter the marks: "))
    l1=[rollno,name,marks]
    headers.append(l1)
print(tabulate(headers, tablefmt="pretty"))
print(headers[1])
