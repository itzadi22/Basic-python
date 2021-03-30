# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:14:50 2021

\w:-word
\W:-Non word(special character)

@author: ASUS
"""

import re

string="#cricket,I love playing cricket @chinnaswamystadium "

s1=re.findall("\w+", string)
print(s1)

s2=re.findall("\W+", string)
print(s2)



