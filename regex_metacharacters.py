# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:51:54 2021

\d Digit
\D Non Digit

@author: ASUS
"""

import re

string="#cricket,I love you cricket 10 times"

s1=re.findall("\d+", string)
print(s1)

s2=re.findall("\D+", string)
print(s2)


