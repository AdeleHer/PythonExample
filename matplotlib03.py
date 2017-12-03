# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:00:12 2017

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,5.,0.2)
# 'r--' 紅色虛線 'bs' 藍色方格 'g^' 綠色三角形
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()