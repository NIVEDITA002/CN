# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:49:12 2022

@author: 20pc25
"""

import math

dataword = input("Enter the data bits : ")

d = len(dataword)

p = int(math.log2(d))

c = d + p

codeWord = []

dw = 0

for i in range(c+1):
    codeWord += " "
    
print(codeWord)
    
for i in range(p+1):
    codeWord[pow(2,i)-1] = "P"
    
print(codeWord)
    
for i in range(c+1):
    if codeWord[i] == ' ':
        codeWord[i] = dataword[dw]
        dw += 1

print(codeWord)