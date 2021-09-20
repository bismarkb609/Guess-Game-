#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing libraries 
import random 
import math 


# In[ ]:


#taking user inputs
lowValue = int(input("LOWEST VALUE: "))
highValue = int(input("HIGHEST VALUE: "))


# In[ ]:


#generating random between lowValue and highValue 
y = random.randint(lowValue, highValue)
print(f"you have 3 chance to get it right!")


# In[ ]:


#starting the counter 
count = 0 

#user has only 3 chances to get it right 
while count < 3:
    count += 1 
    
    #allowing the user to guess as an input
    guess = int(input("Guess a number: "))
    
    #testing if the user guess correct 
    if y == guess:
        print(f"Congratulations, you guessed right in {count} try")
        
        break
    elif  y < guess:
        print("You guessed too high!")
    elif y > guess:
        print("You guessed too small!")

if count >= 3:
    print(f"The number is {y}")
    


# 
