# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:49:00 2021

@author: ASUS
"""

from datetime import datetime
import pytz

a= pytz.timezone('America/New_York') 
time1= datetime.now(a)
print("NY time:", time1.strftime("%H:%M:%S"))

b= pytz.timezone('Europe/London')
time2= datetime.now(b)
print("London time:", time2.strftime("%H:%M:%S"))

c=pytz.timezone('Asia/Kolkata')
time3=datetime.now(c)
print("Indian time :",time3.strftime('%H:%M:%S'))






