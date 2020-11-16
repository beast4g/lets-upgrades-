#!/usr/bin/env python
# coding: utf-8

# # Question - 1:

# In[ ]:


Create a numpy array starting from 2 till 50 with a stepsize of 3


# In[1]:


# importing numpy with alias name
import numpy as np

# creating a array using numpy arange
arr = np.arange(2, 50, 3)

# printing array
print(arr)


# # Question - 2

# In[ ]:


Accept two lists of 5 elements each from the user. Convert them to numpy arrays.
Concatenate these arrays and print it. Also sort these arrays and print it.


# In[2]:



# importing numpy with alias name
import numpy as np

# creating a 2 empty list:
lst_1 = []
lst_2 = []

# getting values for lst_1 from user:
for i in range(5):
  x=int(input("\nEnter the value for lst_1 : "))
  lst_1.append(x)

# getting values for lst_2 from user:
for i in range(5):
  x=int(input("\nEnter the value for lst_2 : "))
  lst_2.append(x)

# converting list into array:
arr_1 = np.array(lst_1)
arr_2 = np.array(lst_2)

# concatenating 2 array:
arr = np.concatenate((arr_1, arr_2))
print("\nArray value for concatenated arr :",arr)

# sorting up concatenated array
sortArr = np.sort(arr)
print("\nSorted Array for concatenated arr :",sortArr)


# # Question - 3:

# In[ ]:


Write a code snippet to find the dimensions of a ndarray and its size.


# In[ ]:


snippet for finding dimension:


# In[ ]:


ArrayName.ndim


# In[ ]:


snippet for finding size:


# In[ ]:


ArrayName.size


# In[3]:


# importing numpy
import numpy as np

# creating a 2d array
arr = np.array([[1,2,3],[1,3,5]])

# Printing array dimensions (axes)
print("\nDimensions in array : ", arr.ndim)
 
# Printing size of array
print("\nSize of array : ", arr.size)


# # Question - 4
# 
# How to convert a 1D array into a 2D array? Demonstrate with the help of a code snippet
# Hint: np.newaxis, np.expand_dims
# 
# newaxis snippet:
# 
# ArrayName[numpy.newaxis, :] // row major
# 
# 
# ArrayName[:, numpy.newaxis] // column major

# In[4]:


# importing numpy
import numpy as np

# creating a 1d array
arr = np.arange(10)
print("\nShape of Array :",arr.shape)

# converting using newaxis in row wise
row_arr = arr[np.newaxis, :]
print("\nShape of 2d Array in row major :",row_arr.shape)

# converting using newaxis in column wise
col_arr = arr[:, np.newaxis]
print("\nShape of 2d Array in column major :",col_arr.shape)


# In[ ]:


expand_dims snippet:
    
numpy.expand_dims(ArrayName, axis = 0) // row major

numpy.expand_dims(ArrayName, axis = 1) // column major


# In[5]:


import numpy as np

# creating a 1d array
arr = np.arange(10)
print("\nShape of Array :",arr.shape)

# converting using newaxis in row wise
row_arr = np.expand_dims(arr, axis=0)
print("\nShape of 2d Array in row major :",row_arr.shape)

# converting using newaxis in column wise
col_arr = np.expand_dims(arr, axis=1)
print("\nShape of 2d Array in column major :",col_arr.shape)


# # Question - 5:
# 
# Consider two square numpy arrays. Stack them vertically and horizontally.
# 
# Hint: Use vstack(), hstack()
# 

# In[6]:


# importing numpy
import numpy as np

# creating a array with square values
arr_1 = np.square([1, 2, 3, 4, 5])
arr_2 = np.square([6, 7, 8, 9, 10])

# stacking and printing the value
print("\nHorizontal Append :", np.hstack((arr_1, arr_2)))
print("\nVertical Append :", np.vstack((arr_1, arr_2)))


# # Question - 6:
# 
# How to get unique items and counts of unique items?
# 
# unique method in numpy is used to get the unique values from the list and return count attribute of 
# 
# unique method return the count of unique value from the list.
# 

# In[7]:


# importing numpy
import numpy as np

# creating a array 
arr_1 = np.array([1, 4, 9, 16, 25, 1, 4, 2, 3, 2, 5, 6, 5, 7, 8, 10])

# getting unique charater and its count
unique, counts = np.unique(arr_1, return_counts=True)

# making a 
arr = np.asarray((unique, counts)).T

print(arr)

