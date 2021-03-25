# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:46:15 2021

@author: ASUS
"""

import csv
import numbers
list=[]
with open("capital-onebike.csv","r")as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        list.append(row[2])
        print(row[2])    
        