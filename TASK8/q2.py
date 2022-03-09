# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:10:27 2022

@author: Dell
"""

import numpy as np
# Testing two random arrays
# First Array
arr1= np.random.randint(0,2,5)
print("1st array:")
print(arr1)
# Second Array
arr2 = np.random.randint(0,2,5)
print("2nd array:")
print(arr2)
array_equal = np.allclose(arr1, arr2)
print(array_equal)
