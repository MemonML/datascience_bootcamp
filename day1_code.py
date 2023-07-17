#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Commenting the text


# In[2]:


name= input ()
print ("Welcome Mr. "+ name)

hours = input (")
rateperhour = input ()
grosspay= hours*rateperhour
# In[3]:


hours = input (")
rateperhour = input ()
grosspay= hours*rateperhour


# In[6]:


hours = int(input ("enter the hours "))
rateperhour = int(input ("enter rate per hour "))
grosspay= hours*rateperhour
print ("your grosspay is", grosspay)


# In[7]:


celcius= input ("enter the celcius temprature")


# In[10]:


celcius= int (input ("enter the celcius temprature"))
farhenheit= (celcius * 9/5) + 32
print ("The Farhenheit Temprature is =", farhenheit ,"F")


# In[20]:


first_name= input ('Enter your first Name')
last_name= input ('Enter your last Name')
complete_name= first_name +" "+ last_name 


# In[21]:


print ('Your compelete Name is', complete_name)


# In[22]:


## Expressions ##

5==5


# In[26]:


x= 2
y= 3
x==y


# In[27]:


x!=y


# In[28]:


x is y


# In[29]:


x and y


# In[31]:


x>0 and x<10


# In[32]:


not (x>y)


# In[33]:


not (x<y)


# In[37]:


x= int (input ('input an integer '))
if x <10:
    print ('x is less than 10')


# In[39]:


x=10
y=10
if x<y:
    print ('x is less than y')
elif x>y:
    print ('x is greated than y')
else:
    print ('x and y are equal')


# In[45]:


x=10
y=10
if x==y:
    print ('x and y are equal')
else :
        if x<y:
        print ('x is less than y')
            else:
                print ('x and y is greated')


# In[53]:


inp = input ('Enter Farhenheit Temprature:')
try:
    far = float (inp)
    cel = (far- 32.0) * 5.0 /9.0 
    print(cel)
except:
    print ('Please enter a number')


# In[63]:


score= float (input ('Enter a value beterr 0.0 to 1.0'))
if score >= 0.0 and score <1.0:
    print ('You have entered right value')
    if score >=0.9:
        print (' Your grade is A  = on your given score ', score)
    elif score >= 0.8 :
        print (' Your grade is B  = on your given score ', score)
    elif score >= 0.7 :
        print (' Your grade is C = on your given score ', score)
    elif score >= 0.6 :
        print (' Your grade is D = on your given score ', score)
    elif score >= 0.5 :
        print (' Your grade is F = on your given score ', score)
else: 
    print ('please enter the correct value')


# In[64]:


import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# In[65]:


import math as ma
degrees = 45
radians = degrees / 360.0 * 2 * ma.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# In[66]:


from math import pi,sin
degrees = 45
radians = degrees / 360.0 * 2 * ma.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# In[69]:


import random
for i in range (10):
    x= random.randint(5,10)
    print (x)

print (x)
# In[76]:


t= ['Mudasar', 'Latif', 'Memon']
random.choice(t)


# In[77]:


def print_fullname(first_name, last_name)
print (first_name)
print (last_name)

print_fullname()


# In[78]:


def print_fullname(first_name, last_name)
print (first_name)
print (last_name)


# In[79]:


def print_fullname(first_name, last_name):
print (first_name)
print (last_name)


# In[84]:


def print_fullname(first_name, last_name):
    print (first_name)
    print (last_name)

    return (first_name, last_name)
print_fullname('Mudasar', 'Latif')


# In[ ]:




