#!/usr/bin/env python
# coding: utf-8

# # Question-1

# given the following jumbled word,OBANWRI guess the correct english word.
# 
# A.RANIBOW
# 
# B.RAINBOW
# 
# C.BOWRANI
# 
# D.ROWVANI
# 
#    ANSWER:B.RAINBOW

# # Question-2

# In[ ]:


write a program which prints"LETS UPGRADE".(please note that you have to print in ALL CAPS as given)


# In[1]:


print("LETS UPGRADE")


# # Question-3

# In[ ]:


write a program that takes cost prices and selling price as input and displays whether the transaction is a profit or
a losses or neither.


# In[14]:


#getting cost price and selling price from user
cost_price=int(input())
selling_price=int(input())


# In[18]:


#condition for checking profit or loss or neither using if-elif sttement.
   
if cost_price<selling_price:
       print("profit")
       
elif cost_price>selling_price:
       print("loss")
       
else:
       print("Neither")


# In[ ]:





# # Question-4

# In[ ]:


write a program that takes an amount in euros as input.you need to find its equivalent in rupees and displays it.assume
1 euro equals Rs.80


# In[19]:


#getting value of euro from user.
euro=int(input())


# In[21]:


#converting the euro into rupees assuming 1 euro = Rs.80.
rupees = euro * 80

#printing the value after converting euro into rupees.
print(rupees)


# In[ ]:




