#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''Assignment 0

This assignment is a giveaway assignment.
By completing this assignment, you will familiarize yourself with this
    course's submission mechanics.
'''

def three_number_average(x, y, z):
    '''Item 1.
    Three Number Average. 3 points.

    Returns the average of three numbers.

    Parameters
    ----------
    x: int
        the first number
    y: int
        the second number
    z: int
        the third number

    Returns
    -------
    float
        the average of x, y, and z
    '''
    # Write your code below this line 
    n1 = int(input("enter first value:"))  
    n2 = int(input("enter second value:"))
    n3 = int(input("enter third value:"))
    avaln = (n1+n2+n3)/3
    print("the average is:",avaln)
    
