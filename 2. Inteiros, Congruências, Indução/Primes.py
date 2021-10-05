# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:02:27 2019

@author: Joana
"""
num = 150
f = 13331
l = []
for i in range(4,num):
    for n in range(2,num):
        if (i % n) == 0:
            break
        elif n == i - 1:
            l.append(i)
            break

for s in l:
    if f%s == 0:
        print(s)
    