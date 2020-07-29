# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:40:30 2020

@author: Adriana
"""

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('wktime.T001.his',delim_whitespace=True)
data2=pd.read_csv('wktime.T004.his',delim_whitespace=True)

y=data.ix[:,1]
x=data2.ix[:,1]
#print(data)
#print(x)
#print(y)
plt.plot(y, color='green', linestyle='solid',markersize=12)
plt.plot(x,color='blue', linestyle='solid', markersize=12)
plt.xlim(1e-3,2e2)
plt.ylabel('p(w)')
plt.xlabel('w')
plt.yscale('log')
plt.show()
