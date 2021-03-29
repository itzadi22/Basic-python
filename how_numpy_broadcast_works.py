# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:05:21 2021

@author: ASUS
"""
import numpy as np


#initialize 'x'
x=np.ones((3,4))
print(x)
print(type(x))

#check shape of x
print(x.shape)

#Initialize Y
y=np.random.random((3,4))
print(y)

#check shape of Y
print(y.shape)

#Add x and y

print(x+y)
