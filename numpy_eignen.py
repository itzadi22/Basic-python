# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:01:54 2021

@author: ASUS
"""

import numpy as np
a=np.array([[4,8],
            [6,26]])
print(a)

eigenval,eigenvec=np.linalg.eig(a)
print(eigenval,eigenvec)
