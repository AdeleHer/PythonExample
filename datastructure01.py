# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:07:17 2017

@author: admin
"""

import numpy as np
from scipy import linalg

A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(A)
print(linalg.inv(A))
print(A.dot(linalg.inv(A)))