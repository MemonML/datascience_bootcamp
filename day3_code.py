#!/usr/bin/env python
# coding: utf-8

# In[31]:


#%Format Specifiers

camels=42
'I have %d camels' %camels


# In[16]:


print ('{:d}'.format(10))


# In[17]:


print ('{:.2f}'.format(0.5))


# In[19]:


# values replace
c=1
'a b c %d a b c'%c


# In[23]:


'{:.2f}'.format(0.5)


# In[24]:


# display 2 spaces
'{:.2s}'.format('python')


# In[25]:


# display total of 6 spaces at the right
'{:<6s}'.format('py')


# In[26]:


# display total of 6 spaces at the left
'{:>6s}'.format('py')


# In[27]:


# display total of 6 spaces at the center
'{:^6s}'.format('py')


# In[43]:


# Files (Open, Read, Write, Close)

fhand = open('C:/Users/Mudasar/mlm1.txt')
print(fhand)


# In[44]:


# Reading files
fhand= open('C:/Users/Mudasar/mlm1.txt')
count=0
for line in fhand:
    count= count+1
print ('Line Count: ',count)


# In[45]:


dir (fhand)


# In[49]:


# Check the length of the file
fhand= open('C:/Users/Mudasar/mlm1.txt')
inp=fhand.read()
print(len(inp))


# In[50]:


# Check the content of the file
fhand= open('C:/Users/Mudasar/mlm1.txt')
inp=fhand.read()
print(inp)


# In[56]:


# Searching in text
fhand= open('C:/Users/Mudasar/mlm1.txt')
count=0
for line in fhand:
    if line.startswith('7'):
        print(line)


# In[61]:


# Dynamic file path
fname= input ('Enter the file name')
fhand= open (fname)
count=0
for line in fhand:
      if line.startswith('7'):
        count=count+1
print(' There were', count, 'lines in', fname)


# In[64]:


# Opening file from Dynamic file path
fname= input ('Enter the file name')
try:
    fhand= open (fname)
    count=0
    for line in fhand:
      if line.startswith('7'):
        count=count+1
    print(' There were', count, 'lines in', fname)
except:
    print('please enter the correct file name')


# In[65]:


# Writing in a file = it will delete all content in file
fout= open('C:/Users/Mudasar/mlm1.txt', 'w')
print(fout)


# In[70]:


# Writing in a file
fout= open('mlm2.txt', 'w')
print(fout)


# In[74]:


line1= "This is new text for file, \n"
fout.write(line1)


# In[77]:


# reading the file
fout= open('C:/Users/Mudasar/mlm2.txt')
fout.read()


# In[78]:


# Create a py extension file
fout= open('shout2.py', 'w')
print(fout)


# In[81]:


# List
cheeses= ['chaddar','Edam','Gouda']
numbers= [17,123]
empty=[]
print (cheeses, numbers, empty)


# In[83]:


# List 
cheeses= ['cheddar','Edam','Gouda']
numbers= [17,123]
empty=[]
print (cheeses[0], numbers, empty)


# In[84]:


# list are mutable

numbers= [17,123]
numbers[1]=5
print (numbers)


# In[85]:


# list are mutable, updating multiple elements

numbers= [17,123,55,67]
numbers[1:2]=5, 6
print (numbers)


# In[86]:


# Traversing a list
numbers=[1, 2, 3, 4, 5, 6, 7, 8]
for i in numbers:
    print (i)


# In[91]:


# list are mutable, updating multiple elements

numbers= [17,123,55,67]
numbers[1:2]= [5, 6]
print (numbers)


# In[95]:


a=[1,2,3,4,5,6,7]
a[0]=[8,9,10,11,12,13]
print(a)


# In[96]:


a=[1,2,3,4,5,6,7]
a[0]=[8,9,10,11,12,13],[14,15,16,17,18]
print(a)


# In[97]:


# Using Range function in List
numbers= [17,123,55,67]
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2
print(numbers)


# In[98]:


# List concatenation
a= [1,2,3]
b=[4,5,6]
c=a+b
print (c)


# In[99]:


# Multiplication in list
[0]*4


# In[100]:


# Multiplication in list
[1,2,3,4]*4


# In[101]:


# List Slices
t=['a','b','c','d','e','f']
print(t[1:3])
print (t[:3])
print (t[:4])
print (t[3:])


# In[103]:


# List Slices Iteration
t=['a','b','c','d','e','f']
print(t[1:3:2])
print(t[1:6:2])


# In[104]:


# List Slices Iteration
t=['a','b','c','d','e','f']
print(t[::2])


# In[106]:


t=['a','b','c','d','e','f']
print(t[::-2])


# In[107]:


# Append will add the element in the last of a list
t= ['a','b','c']
t.append('d')
print(t)


# In[113]:


# extend will concatenate the list
t1= ['a','b','c']
t2=['e','f']
t1.extend(t2)
print(t1)


# In[114]:


# Sorting in list
t= ['d','c', 'e','b','a']
t.sort()
print(t)


# In[115]:


# Sorting in list
t= [5,3, 8,7,1]
t.sort()
print(t)


# In[116]:


# Sorting in list
t= ['Mudasar','Banana','Apple','Cat','bat']
t.sort()
print(t)


# In[117]:


# Sorting in list (donot sort the mixed data type characters)
t= ['Mudasar','Banana','Apple','Cat','bat',1,9,7,2,'f','e','c']
t.sort()
print(t)


# In[119]:


# pop
t= ['d','c', 'e','b','a']
x=t.pop(1)
print(t)
print(x)


# In[120]:


# Delete an element
t= ['d','c', 'e','b','a']
del t[1]
print(t)


# In[121]:


# Remove an element

t= ['d','c', 'e','b','a']
t.remove('b')
print(t)


# In[122]:


# Builtin function in pyhton (max, min, sum)

num= [5,3, 8,7,1]
print (len(num))

print (max(num))

print(min(num))

print (sum(num))

print (sum(num)/len(num))


# In[123]:


# Calculating the average with list
numlist =list()
while(True):
    inp = input ('Enter a number:')
    if inp == 'done': break
    value= float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)


# In[124]:


# Converting a string into list
s='spam'
t=list(s)
print(t)


# In[131]:


# Converting a string into list
s='Pakistan'
x= [i for i in s]
x


# In[127]:


# Split command
s= 'spam-spam-spam'
delimiter= '-'
print (s.split(delimiter))


# In[128]:


# Split command
s= 'spam spam spam'
delimiter= ' '
print (s.split(delimiter))


# In[129]:


t= ['pining', 'for', 'the', 'fjords']
delimiter= ' '
print(delimiter.join(t))


# In[ ]:




