# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:41:41 2021

HISTOGRAM

@author: ASUS
"""

from matplotlib import pyplot as plt
 
plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [6,8,12,5,7,9,18,0,2,5,10,12,15,4,4,14,18,10,15,14])
x=[4,8,14,14,19]
y=[6,1,5,6,16]
plt.scatter(x,y)
plt.xlabel("overs")
plt.xticks(range(0,21))
plt.ylabel("runs")
plt.yticks(range(0,20))
plt.title("INDIA")

plt.show()


