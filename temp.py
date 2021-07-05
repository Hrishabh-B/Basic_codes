#This code is written for dynamic step-size. step size c0 gets smaller when it achieves the number 200.
#Author: Hrishabh Bharadwaj, Senior Research Fellow, University of Delhi
#Date: 5-07-2021
from math import *
import numpy as np

c0=50.0

for x in np.arange(c0,580,10):
    t=10*(abs(200.1-c0)/200.1)*abs(np.log(0.3/abs(c0-200.1)))
    y=1.0/(c0-200.0**2)**2
    print(str(c0)+"   "+str(y))
    c0+=t
    if c0> 198 and c0<202:
        c0+=1
        


