# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:27:41 2021

The bool() method in general takes only one parameter(here x), 
on which the standard truth testing procedure can be applied.
If no parameter is passed, then by default it returns False. 
So, passing a parameter is optional. It can return one of the two values. 

It returns True if the parameter or value passed is True.
It returns False if the parameter or value passed is False.
Here are a few cases, in which Python’s bool() method returns false.
Except these all other values return True. 

If a False value is passed.
If None is passed.
If an empty sequence is passed, such as (), [], ”, etc
If Zero is passed in any numeric type, such as 0, 0.0 etc
If an empty mapping is passed, such as {}.
If Objects of Classes having __bool__() or __len()__ method, returning 0 or False
 

@author: ASUS
"""
# Python program to illustrate
# built-in method bool()

# Returns False as x is False
x = False
print(bool(x))

# Returns True as x is True
x = True
print(bool(x))

# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x==y))
