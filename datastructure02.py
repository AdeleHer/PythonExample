# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:29:34 2017

@author: admin
"""

import numpy as np
from scipy import linalg as ll

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(A)
print(ll.det(A))