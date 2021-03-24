# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:42:25 2021

Difference between two dates

@author: ASUS
"""

import datetime
data1 = datetime.datetime(2000, 12, 22)
data2 = datetime.datetime(2000, 12, 25)

diff = data2 - data1

days=diff.days
hours = days * 24
print(hours)



