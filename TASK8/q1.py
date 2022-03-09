# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:58:22 2022

@author: Dell
"""

import numpy as np
data = np.array([10,11,12,13,14])
print("data:")
k=5
new_data = np.zeros(len(data) + (len(data)-1)*(k))
new_data[::k+1] = data
print("\nNew array:")
print(new_data)

