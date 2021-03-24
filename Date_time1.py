# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:36:48 2021
Time 
@author: ASUS
"""

import time
print(time.time())
print(time.ctime(1616558945.256669))
print(help(time.time))
a=(time.localtime())
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
d=time.strftime("%d/%m/%Y")
print(d)
e=time.strftime("%d/%m/%Y")
print(e)
f=time.strftime("%j")
print(f)

