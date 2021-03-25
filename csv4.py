# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:53:34 2021

@author: ASUS
"""

import csv
startstation=[]
with open("capital-onebike.csv","r")as file:
    reader=csv.reader(file)
    header=next(reader)
    for column in reader:
        startstation.append(column[3])
        print(column[3])
        
        
        
        