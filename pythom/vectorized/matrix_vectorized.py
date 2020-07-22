# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:51:10 2020

@author: Adriana
"""

import numpy as np
#declaramos las matrices
M1=np.array([[4,7],[4,4],[9,1]]) #matriz m1
M2=np.array([[1,2,3],[3,7,5]])  #matriz m2
#multiplicamos las matrices
dn=np.dot(M1,M2)
#imprimimos
print(dn)



