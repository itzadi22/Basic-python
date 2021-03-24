# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:12:40 2021

@author: ASUS
"""

from datetime import datetime

date_time_str = '18/09/19'
date1=input("Enter date 1 (YYYY-MM-DD) :")
date2=input("Enter date 2 (YYYY-MM-DD) :")

date_time_obj1 = datetime.strptime(date1, '%Y-%m-%d')
date_time_obj2 = datetime.strptime(date2, '%Y-%m-%d')
diff=date_time_obj2-date_time_obj1
print("The difference between two dates is : ",diff)


