# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:40:54 2019

@author: Joana
"""

def batch_norm(alist, batch_size):
    while len(alist) >= batch_size:
        a = alist[:batch_size]
        n = sum(a)/len(a)
        alist = alist[batch_size:]
        yield list(map(lambda x: round(x - n), a))
    if alist == []:
        pass
    else:
        n = sum(alist)/ len(alist)
        yield list(map(lambda x: round(x - n), alist))
        
print(list(batch_norm(    [-1, 0, 1, 1, 2, 4], 3)))