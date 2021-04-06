# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:46:39 2021

Check if any of the items in a list are True:

Definition:-
The any() function returns True if any item in an iterable are true,
 otherwise it returns False.

If the iterable object is empty, the any() function will return False.

Syntax:
any(iterable)

@author: ASUS
"""
a=(1,13,0)
print(any(a))


mylist = [False, True, False]
x = any(mylist)
print(x)


b={False,0}
print(any(b))
 
c={False,1,0,False}
print(any(c))