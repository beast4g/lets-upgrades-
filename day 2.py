#!/usr/bin/env python
# coding: utf-8

# # Question - 1:

# In[ ]:


Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.


# In[1]:


# creating a empty list
lst = []


# getting 10 values from user
for i in range(0,10):
    x = int(input("\nEnter the value : "))
    lst.append(x)
    
# creating a empty list to append event numbers
even_lst = []

# appending only even numbers
for i in lst:
    if(i%2==0):
        even_lst.append(i)
        
print("\nThe even list",even_lst)


# # Question - 2

# In[ ]:


Create a notebook on LIST COMPREHENSION. This exercise is to put you in a Self learning mode


# In[ ]:


List comprehensions are used for creating new lists from other iterables.


# In[ ]:


As list comprehensions return lists, they consist of brackets containing the expression, which is executed
for each element along with the for loop to iterate over each element


# # Syntax:

# In[ ]:


new_list = (value for_loop condition)


# # Example:

# In[2]:


# creating a list
lst = [1, 2, 3, 4, 5, 6, 7, 8]

# list comprehensions
even_lst = [i for i in lst if i%2==0 ]

print(even_lst)


# # Question - 3:

# In[ ]:


Given a number n, you have to write a program that generates a dictionary d which contains (i, i*i),
where i is from 1 to n (both included).


# In[3]:


# creating a empty dict
dict = {}

#  getting value for "n" from user
n = int(input())

for i in range(1,n+1):
  dict[i] = i*i

print(dict)


# # Question - 4:

# In[ ]:


Write a program to compute the distance between the current position after a sequence of movement and original 
point.If the distance is a float, then just print the nearest integer (use round() function for that and
then convert it into an integer).


# In[4]:


#  creating a origin position
pos = {"x":0,"y":0}

# getting movement from user
n = int(input())

# for loop
for i in range (n):
    move =  input().split(" ")      # ACCEPT MOVEMENT COMMAND AND STORE AS A LIST
    
    if move[0].lower() == "up":     # EXTRACT DIRECTION AND COMPARE
        pos["y"] += int(move[1])    # INCREMENT/DECREMENT APPROPRIATE CO-ORDINATES
    
    elif move[0].lower() == "down":
        pos["y"] -= int(move[1])
    
    elif move[0].lower() == "left":
        pos["x"] -= int(move[1])
    
    elif move[0].lower() == "right":
        pos["x"] += int(move[1])

#  printing the result

print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)))   # DISTANCE FROM ORIGIN

