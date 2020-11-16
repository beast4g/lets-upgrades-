#!/usr/bin/env python
# coding: utf-8

# # Question - 1:
# 
# How to import pandas and check the version?
# 
# "import pandas" is importing statement used in python which is used to import the pandas module.
# 
# print(pandas.version ) is used to print the version of the pandas module imported.
# 

# In[1]:


# importing pandas with alias name
import pandas as pd

# printing the version of pandas
print(pd.__version__)


# # Question - 2
# 
# How to create a series from a numpy array?
# 
# A series can be created from numpy array using 2 different way:
# 
# .using only numpy array value
# .using only numpy array value along user index value

# In[2]:


# importing numpy and pandas with alias name
import numpy as np
import pandas as pd

# using numpy array value
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
# creating series from array 
series = pd.Series(data) 
print(series)


# In[3]:


# importing numpy and pandas with alias name
import numpy as np
import pandas as pd

# using numpy array value
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
# creating series from array with user index value
series = pd.Series(data, index = [1, 2, 3, 4, 5]) 
print(series)


# # Question - 3:
# 
# How to convert the index of a series into a column of a dataframe?¶

# In[4]:


# importing numpy and pandas with alias name
import numpy as np
import pandas as pd

# using numpy array value
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
# creating series from array with user index value
series = pd.Series(data, index = [1, 2, 3, 4, 5]) 

# convert series to dataframe 
df = series.to_frame().reset_index() 
  
# show the dataframe 
df


# # Question - 4:
# 
# Write the code to list all the datasets available in seaborn library.
# 
# Load the 'mpg' dataset

# In[6]:


# importing seaborn
import seaborn as sns

mpg=sns.load_dataset('mpg')

print(mpg)


# # Question - 5:
# 
# Which country origin cars are a part of this dataset?¶

# In[7]:


# importing seaborn
import seaborn as sns
# importing pandas with alias name
import pandas as pd

# loading the dataset from seaborn
mpg=sns.load_dataset('mpg')

# creating a dataframe
df = pd.DataFrame(mpg)

# Displaying the country origin from where cars belong
df.origin.unique()


# # Question - 6:
# 
# Extract the part of the dataframe which contains cars belonging to 'usa'

# In[8]:


# importing seaborn
import seaborn as sns
# importing pandas with alias name
import pandas as pd

# loading the dataset from seaborn
mpg=sns.load_dataset('mpg')

# creating a dataframe
df = pd.DataFrame(mpg)

# Displaying the part from dataframe where cars belong to "usa"
df[df['origin'].str.contains("usa")]

