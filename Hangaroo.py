#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HANGAROO game

name = input("What is your name? ") 
print ("Hello, ",'avi', "\nLets play Hangaroo!" )

print ("\nStart guessing...") 
 
word = "secret" 
guesses = ''
turns = 3
while turns > 0: 
    failed = 0
    for char in word:
        if char in guesses:
            print (char, end = ' ') 
        else:
            print ("_", end = ' ')
            failed = 1 
    
    if failed == 0: 
        print("\nYou won") 
        break
        
    print('\n')
    guess = input("guess a character: ")
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", turns, 'more guesses')

if turns == 0:
    print ("You Lose")


# In[ ]:




