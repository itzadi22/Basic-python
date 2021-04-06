# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:21:38 2021

all() function:-
1.Check if all items in a list are True:
2.Note: When used on a dictionary, the all() function checks if all 
  the keys are true, not the values.
3.The all() function returns True if all items
  in an iterable are true, otherwise it returns False.
  If the iterable object is empty, the all() function also returns True.
4.	An iterable object may be (list, tuple, dictionary)

@author: ASUS
"""

a=[1]
print(all(a))

b=[0]
print(all(b))

c=[]
print(all(c))

d=(1,2,True)
print(all(d))

e={1,2,True,0}
print(all(e))

f=(1,2,10)
print(all(f))

