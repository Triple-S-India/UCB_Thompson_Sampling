#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Random Selection

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('D:DS_TriS/Ads_CTR_Optimisation.csv')

# Implementing Random Selection
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()


# In[15]:


total_reward


# In[14]:


#We we use random selection than our rewards is very less 
#and plot is showing that it's not a good solution.
#So, for better result we are going to use UCB(Upper Confidence Bound)


# In[1]:


#Upper Confidence Bound


# In[2]:


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


# Importing the dataset
dataset = pd.read_csv('D:DS_TriS/Ads_CTR_Optimisation.csv')


# In[4]:


dataset.head()


# In[5]:


dataset.isnull().sum()


# In[6]:


dataset.shape


# In[7]:


# Implementing UCB
import math
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward


# In[8]:


ads_selected[25:35]


# In[9]:


sums_of_rewards


# In[10]:


total_reward


# In[11]:


# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')


# In[16]:


#So here we have almost doubled our total rewards than the Random Selection 
# and plot clearly shows that 5th(id5, index 4) is most profitable ad.


# In[ ]:




