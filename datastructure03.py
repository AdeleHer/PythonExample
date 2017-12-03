# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:43:32 2017

@author: admin
"""

import numpy as np
from scipy import linalg as la

A = np.array([[1,5,2],[2,4,1],[3,6,2]])
lna,v = la.eig(A)
l1,l2,l3 = lna
#EigenValue
print(l1,l2,l3)
#EigenVector
print(v)
print(v[:,0])
print(v[:,1])
print(v[:,2])
v1 = np.array(v[:,0]).T
print(v1)
print(la.norm(A.dot(v1)-l1*v1))