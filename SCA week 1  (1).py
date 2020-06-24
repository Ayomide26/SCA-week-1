#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Guess a number
import random
numofguesses = 0
number= random.randint(1,20)
#while numofguesses < 6:
print("take a guess.")
guess=input()
guess =int(guess)
numofguesses = numofguesses + 1
if guess < number:
        print("NUmber is too Low")
if guess > number:
        print("NUmber is too High")
if guess == number:
        print("You guessed right")
        
    


# In[ ]:


# In[ ]:





# In[ ]:




