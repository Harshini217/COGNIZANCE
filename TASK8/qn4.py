import numpy as np
import pandas as pd 

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])

st = ser.str.capitalize()
print(st)
