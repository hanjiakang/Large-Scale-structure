#!/usr/bin/env python
# coding: utf-8

# In[101]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
import sys, platform, os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import camb
from camb import model, initialpower
from camb import correlations
import numpy as np
from scipy.special import spherical_jn as jn
from scipy.special import sph_harm as sph
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.rcParams['text.usetex'] = False
#import the module


# In[102]:


phi=0
theta=0
m=0       
#to make it simpler i just chose all of these parameter to be zero
em=np.zeros(2000)
#create the numpy array that could be used to store the result from each those orders
leg=[]
#create the list to store the l value respectively
for n in range(4):
    #since only the odd number orders contribute to the imaginary part
    #2n+1 is all the odd number less than 10
    l=2*n+1
    x=np.arange(0,20,0.01)
    el=4*np.pi*np.sqrt((2*l+1)/4/np.pi)*jn(l,x)*sph(0,l,0,0)
    em=em+el#adding up all the mode
    plt.plot(x,el)#plot the mode of order l
    s='l={l}'
    s=s.format_map(vars())
    leg.append(s)
plt.legend(leg)
plt.xlabel("$ \chi $")
plt.ylabel(r"$4\pi\sqrt{\frac{2l+1}{4\pi}}j_l(kx)Y_l0( \Theta=0,\phi=0)$")
plt.title("series expension with only imaginary part")
plt.figure()
plt.plot(x,em)
plt.title(r"imaginary part of $e^{i(\hat{k} \cdot \hat{n})k\chi}$")
plt.xlabel("$\chi$")
plt.ylabel("$Im(e^{i(\hat{k}}\cdot\hat{n})k\chi}$")


# In[54]:





# In[ ]:




