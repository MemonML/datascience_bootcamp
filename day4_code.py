#!/usr/bin/env python
# coding: utf-8

# In[10]:


# List  Arguments
t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)
t3= t1+ [3]
print (t3)
t2 is t3


# In[11]:


# List  Arguments
t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)
t3= t1+ [3]
print (t3)
t2 is t3
t4=[1,2,3]
print(t4)
t1 is t4


# In[12]:


# List  Arguments
t5 = ['a','b']
t6 = t5.append('c')
print(t5)
print(t6)
t7= t5+ ['c']
print (t7)


# In[19]:


# List  Arguments, appending on the same location of memory, if we change one variable t2, other variable t1 will
# be updated automatically, due to same memory location
t7 = ['a','b']
t8 = t7
print(t7)
print(t8)
t7 is t8
t8.append ('c')
print(t7)
print(t8)


# In[24]:


# Tuples , it is like a static variable (imutable), could not be changed, where as list is dynamic

# empty tuple
my_tuple=()
print (my_tuple)

# Tuples having integers
my_tuple1=(1,2,3)
print(my_tuple1)

# Tuple with mixed data types
my_tuple2=(1, 'hello', 1.4)
print(my_tuple2)

# Nested Tuple 
my_tuple3= ('mouse', [1, 2, 3], (4, 5, 6))
print(my_tuple3)
type(my_tuple3)


# In[27]:


# Tuple also accepts without parenthesis

# Tuples having integers
my_tuple1= 1,2,3
print(my_tuple1)
type(my_tuple1)


# In[28]:


# Tuple with mixed data types # Tuple also accepts without parenthesis
my_tuple2= 1, 'hello', 1.4
print(my_tuple2)
type(my_tuple2)


# In[29]:


# Nested Tuple # Tuple also accepts without parenthesis
my_tuple3= 'mouse', [1, 2, 3], (4, 5, 6)
print(my_tuple3)
type(my_tuple3)


# In[33]:


# Tuples do not consider values without commas
my_tuple1= 1
print(my_tuple1)
type(my_tuple1)


# In[36]:


# Tuples do not consider values without commas
my_tuple1= 'movies'
print(my_tuple1)
type(my_tuple1)


# In[38]:


# Accessing the tuples with negative indices, 0 is left most, -1 is the extreme right position
letters= ('p','q','r','h','g','k')
print(letters[-1])
print(letters[-3])
print (letters[0])


# In[39]:


# Accessing the tuples with slicing

letters= ('p','q','r','h','g','k')
print(letters[::-1])
print(letters[1:2:])
print(letters[1:2:-3])


# In[45]:


# Converting the tuple to list

letters= ('p','q','r','h','g','k')
print (letters)
type(letters)

b= list(letters)
print (b)
type (letters)


# In[49]:


# Update the element in the list of a tuple
my_tuple3= 'mouse', [1, 2, 3], (4, 5, 6)
print(my_tuple3[1])
my_tuple3[1][2]=6
print (my_tuple3[1][2])
print(my_tuple3[1])


# In[50]:


dir(my_tuple3)


# In[52]:


# Count & Index command in tuple
letters= ('p','q','r','h','g','k')
print (letters.count('q'))

print(letters.index('r'))


# In[53]:


# iterating in tuples
languages =('python', 'swift','C++')
for language in languages:
    print(language)


# In[56]:


# finding C# in tuple

languages =('python', 'swift','C++')
print ('C' in languages)
print('python' in languages)

for language in languages:
    print('C' in languages)


# In[57]:


# Searches in a a string of a tuple
languages =('python', 'swift','C++')
print ('C' in 'C++')


# In[60]:


# Aliasing is mutable
a=[1,2,3]
b=a
c=b
c is a


# In[63]:


# Dictionaries {} curly braces

# There is no index in dictionaries: Key-value pairs: Key is similiar to index but assinged by user

#Creating Dictionary
my_dict={'key1': 'value1','key2': 'value2', 'key1': 'value1'}

memon_dic={1: 'Mudasar',2: 'Latif', 3: 'Memon'}
print (memon_dic[1])


# In[69]:


#Modifying dictionary values
memon_dic={1: 'Mudasar',2: 'Latif', 3: 'Memon'}

memon_dic[2]= 'LATEEF'
print (memon_dic[2])
print(memon_dic)
type(memon_dic)


# In[70]:


# Data types 
#1. Structured (Having fixed rows and colums)
# 2. Semi-structured (Having some information and can be accessed with some of the parameters)
#3. Unstructured 


# In[72]:


# Creating Dictionary using dict() constructor
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
print(another_dic)


# In[74]:


# Adding a new key-value pair
another_dic['occupation']='Engineer'
print(another_dic)


# In[75]:


# Removing a new key-value pair
del another_dic['age']
print(another_dic)


# In[77]:


# Operations on dictionary
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
len(another_dic)


# In[79]:


# Operations on dictionary
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
print(len(another_dic))
print ('name' in another_dic)


# In[84]:


# Getting the keys
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
key= another_dic.keys()
print(key)


# In[86]:


# Getting the Values
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
value= another_dic.values()
print(value)


# In[89]:


# Getting the Key-Value pairs
another_dic= dict(name='Mudasar', age='36', city='Islamabad')
item= another_dic.items()
print(item)


# In[91]:


# Updating the dictionary
another_dic.update({'occupation':'engineer'})
print(another_dic)


# In[93]:


# Nested Dictionary
dic1= dict(name='Mudasar', age='36', city='Islamabad')
dic2=dict(profession='engineer', gender='male', country= 'Pakistan')
dic1.update(dic2)
print (dic1)



# In[94]:


# Nested Dictionary
person= {'person':{1:{'name':'A', 'age':20, 'occupation':'Software'}, 2:{'name':'B', 'age':21, 'occupation':'CS'}, 3:{'name':'C', 'age':22, 'occupation':'Dev'} }}
print (person)


# In[95]:


# Iterating over keys
dic1= dict(name='Mudasar', age='36', city='Islamabad')
for key in dic1:
    print(key)


# In[98]:


# Iterating over values
person= {'person':{1:{'name':'A', 'age':20, 'occupation':'Software'}, 2:{'name':'B', 'age':21, 'occupation':'CS'}, 3:{'name':'C', 'age':22, 'occupation':'Dev'} }}
for value in person.values():
    print(value)


# In[99]:


# Iterating over values
person= {'person':{1:{'name':'A', 'age':20, 'occupation':'Software'}, 2:{'name':'B', 'age':21, 'occupation':'CS'}, 3:{'name':'C', 'age':22, 'occupation':'Dev'} }}
for item in person.items():
    print(item)


# In[100]:


person= dict(name='Mudasar', age='36', city='Islamabad')
for value in person.values():
    print(value)


# In[101]:


person= dict(name='Mudasar', age='36', city='Islamabad')
for item in person.items():
    print(item)


# In[102]:


person= dict(name='Mudasar', age='36', city='Islamabad')
for key in person.keys():
    print(key)


# In[109]:


# Numpy Library is used for arrays, as python does not have builting arrages, Numpy is for Scientific data, 
# 50x faster than python coz it is made in C/C++

# pandas is used for data manuplation
# scipy
# Scikit-learn

# Convert a list in to numpy array
import numpy as np

list1=[2, 4, 6, 8]
print(list1)
type(list1)

array1= np.array(list1)
print(array1)
type(array1)


# In[117]:


# Create an array of Zeros
import numpy as np

array2=np.zeros(4)
print(array2)
array2.dtype()


# In[123]:


import numpy as np
array4=np.arange(4)
print('using np.arrange(5):',array4)


# In[122]:


import numpy as np
array4=np.arange(4)
print('using np.arange(1,9,2):',array4)


# In[120]:


# Using Random in Numpy array
import numpy as np
array6= np.random.rand(5)
print(array6)


# In[126]:


import numpy as np
array7= np.random.rand(2,2)
print(array7)


# In[129]:


# rand(Slice, Rows, Columns) command in random module of numpy library
import numpy as np
array8= np.random.rand(2,3,4)
print(array8)


# In[133]:


#  empty module in numpy 
import numpy as np
array10= np.empty(1)
print(array10)


# In[134]:


import numpy as np
array10= np.empty(4)
print(array10)


# In[137]:


# Create a 2D Numpy Array with 2 rows and 4 Colums
import numpy as np
array11= np.array([[1, 2, 3, 4 ],[5, 6, 7, 8]])
print(array11)


# In[138]:


# Create a 2D Numpy Array with 2 rows and 4 Colums/ Columns must be same otherwie error
import numpy as np
array11= np.array([[1, 2, 3, 4 ],[5, 6, 7, 8, 9]])
print(array11)


# In[156]:


# Create a 2D Numpy Array with 2 rows and 4 Colums
import numpy as np
array11= np.array([[1, 2, 3, 4 ],[5, 6, 7, 8],[9, 10, 11, 12],
                  [13, 14, 15, 16 ],[17, 18, 19, 20], [21, 22, 23, 24],
                  [25, 26, 27, 28 ],[29, 30, 31, 32], [33, 34, 35, 36]])
print(array11)


# In[142]:


#Multi dimenstional array
import numpy as np
array12= np.random.rand(3,3,3)
print(array12)


# In[150]:


#Multi dimenstional zeros array
import numpy as np
array13= np.zeros((3,2,2))
print(array13)


# In[159]:


#Multi dimenstional array NP arange()
import numpy as np
array14= np.arange(1,17,2)
print(array14)


# In[160]:


import numpy as np
array15= np.full((2,2),5)
print(array15)


# In[161]:


# Create a 3D array with elements initialized to 5 (slince, rows, columns)
import numpy as np
array15= np.full((2,2,2),5)
print(array15)


# In[162]:


# Dimension of array with ndim attribute
array15= np.full((2,2,2),5)
array15.ndim


# In[163]:


array15= np.full((2,2,2),5)
array15.size


# In[164]:


array15= np.full((2,2,2),5)
array15.dtype


# In[165]:


array15= np.full((2,2,2),5)
array15.shape


# In[ ]:




