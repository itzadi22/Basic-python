# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:01:23 2021

@author: ASUS
"""

from matplotlib import pyplot as plt
 
plt.bar([1,3,5,7,9],[50,100,150,200,250],label="Jockey",width=0.5)
plt.bar([2,4,6,8,10],[25,50,150,250,300],label="polo",width=0.5)
plt.xlabel("year")
plt.legend()
plt.ylabel("sales")
plt.yticks(range(0,300,20))
plt.xticks(range(0,11))
plt.title("information")
plt.show()

