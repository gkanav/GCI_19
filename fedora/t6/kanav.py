
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


# In[27]:


a = pd.read_csv('output.csv', header=None)
a.columns = ['x', 'y']

y = a['y'];
x = a['x'];


# In[28]:


plt.xlabel('x');
plt.ylabel('y');
plt.scatter(x,y)
plt.show()

