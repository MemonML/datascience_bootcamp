#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Iteration 
#Execution of While Loop (Infinite Loop untill condition is true)
n=5
while n>0 :
    print (n)
    n=n-1
    print ('Blastoff!')


# In[2]:


# How to break a While Loop "Break Statement" (While is infinite Loop)
while True:
    line = input ('> ')
    if line == 'done':
        break
        print (line)
        print ('Done!')


# In[7]:


# Continue Statement

while True:
    line = input ('> ')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print ('line')
print ('done!')
    


# In[8]:


# For Loop
friends= ['Adeel','Tauseef','Memon']
for friend in friends:
    print ('Happy Ramadhan: ', friend)
print ('Done!')


# In[10]:


# Counting and Summing  Loops
count=0
for intervar in [3, 42, 12, 9, 74, 15]:
    count = count+1
    print ('Count: ', count)


# In[13]:


# Counting and Summing  Loops 2
count=0
for intervar in [3, 42, 12, 9, 74, 15]:
    count = count+1
    print (intervar)
print ('Count: ', count)
    


# In[14]:


# Sum all the values in the list
total=0
for itervar in [3,41,12,9, 74, 15]:
    total = total +itervar
    print ("Total: ", total)


# In[18]:


largest= None
print ('Before: ', largest)
for itervar in [3,41,12,9, 74, 15]:
    if largest is None or  itervar > largest :
        largest = itervar
    print ('Loop:', itervar, largest)
print ("largest:", largest)


# In[19]:


# "None" is Data type in Python

a= None
type (a)


# In[22]:


# Minimum Loops

smallest= None
print ('Before: ', smallest)
for itervar in [3,41,12,9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print ("Loop:", itervar, smallest)
print ('Smallest: ', smallest)


# In[23]:


# Max and Min functions

max([3,41,12,9, 74, 15])


# In[24]:


min([3,41,12,9, 74, 15])


# In[52]:


# Activity 9.1 Enter numbers, add number, count numbers, calculate average, if number is 'done' exit execution. 
total=0
count=0
avergae=0
while True:
    number1 = input ('Enter a number or write done in case you are done > ')
    if number1=='done':
        break
    try:
        number2= int(number1)
        total= total+ number2
        count= count+1
        average=total/count
    except:
        print('The value is not integer, please input the correct value')
print ('The total is = ' , total)
print ('The count is = ', count)
print ('The average is = ', average)


# In[66]:


# Activity 9.2 Multiplication table
num=10
for i in range (1,11):
    print (num, 'x', i, '=', num*i )


# In[63]:


# STRING
a='banana'
a[1]


# In[65]:


# STRING
a='Mudasar'
a[-1]


# In[67]:


fruit = input ('Enter a name of fruit > ')
len(fruit)


# In[68]:


fruit[1]


# In[69]:


# Traversal trough a string with a loop
fruit = 'banana'
index = 0
while index< len (fruit):
    letter= fruit[index]
    print (letter)
    index= index+1


# In[93]:


# Reverse Traversal trough a string with a loop Actvity 10
fruit = 'banana'
index = len(fruit)
while index <= len (fruit):
    letter= fruit[index-1]
    print (letter)
    index= index-1
    if index==0:
        break


# In[94]:


c


# In[97]:


# String Slices
s= 'Mudasar Latif Memon'
print (s[:7])


# In[98]:


# String Slices
s= 'Mudasar Latif Memon'
print (s[0: ])


# In[99]:


# String Slices with increments
s= 'Mudasar Latif Memon'
print (s[0:7:2])


# In[100]:


# String Slices
s= 'Mudasar Latif Memon'
print (s[0:14:3])


# In[103]:


# String Slices Negative Indexing
s= 'Mudasar Latif Memon'
print (s[ :-7])


# In[104]:


# String Slices Negative Indexing
s= 'Mudasar Latif Memon'
print (s[ : : -1])


# In[105]:


# String Slices Negative Indexing
s= 'Mudasar Latif Memon'
print (s[ : -3])


# In[106]:


# Strings are Immutable
greetings= ' Hello world'
greetings[0]='J'


# In[112]:


# Strings are Immutable but can replace
greetings= 'Hello world'
new_greetings= 'J'+ greetings[1:]
print (new_greetings)


# In[113]:


# Looping and Counting
word= 'banana'
count=0
for letter in word:
    if letter == 'a':
        count= count+1
print (count)


# In[116]:


# Activity Count the number of letters 
word= input ('Enter a word> ')
letter1= input ('Enter the letter you want to count> ')
count= 0
for letter in word:
    if letter == letter1:
        count= count+1
print (count)


# In[117]:


# With Function, Count the number of letters
def countletters(str, ch):
    fruit=str
    count=0
    for char in fruit:
        if char == ch:
            count= count+1
    print (count)
countletters ("banana", "a")


# In[118]:


# in Operator returns value True or False
'a' in 'banana'


# In[119]:


'seed' in 'banana'


# In[120]:


# ord function gives ASCII value of characters
print(ord('a'))


# In[124]:


# String Comparison
if word == 'banana':
    print('All right. bannas')


# In[125]:


if word == 'b':
    print('All right. bannas')


# In[126]:


# Compare the ASCII values of Characters
if word < 'b':
    print('All right. bannas')


# In[127]:


if word > 'b':
    print('All right. bannas')


# In[128]:


# Compares the strings on the basis of ASCII value of first character
word= 'pinapple'
if word< 'banana':
    print ('Your word,'+ word + ', comes before banana.')
elif word> 'banana':
    print ('your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')


# In[130]:


ord('p')


# In[131]:


ord ('b')


# In[132]:


# Directory
dir(word)


# In[133]:


# Upper Case
word= 'banana'
new_word= word.upper()
print(new_word)


# In[134]:


# 
word= 'banana'
new_word= word.title()
print(new_word)


# In[135]:


word= 'banana'
new_word= word.split()
print(new_word)


# In[175]:


# Activity 12
# find function finds the character
word= 'banana'
d= word.find('a')

a= word.strip()

b= word.startswith('b')

c= word.lower()

print (a ,'\n', b,'\n', c,'\n', d)


# In[153]:


# Finding @ in the text
text= 'From mudasarlatif.ccnf@iba-suk.edu.pk Sat Jan 5 09:14:16 2008'
text.find('@')


# In[155]:


# split 
text= 'From mudasarlatif.ccnf@iba-suk.edu.pk Sat Jan 5 09:14:16 2008'
text.split()


# In[161]:


# split 
text= 'From mudasarlatif.ccnf@iba-suk.edu.pk Sat Jan 5 09:14:16 2008'
list= text.split()
for i in list:
    print (i)  


# In[162]:


# split 
text= 'From mudasarlatif.ccnf@iba-suk.edu.pk Sat Jan 5 09:14:16 2008'
list= text.split()
for i in list:
    print (i)  
print (list[1])  


# In[177]:


# Write a Python program to convert a given string into a list of words.
text= 'From mudasarlatif.ccnf@iba-suk.edu.pk Sat Jan 5 09:14:16 2008'
list= text.split()
print (list)


# In[179]:


# Write a Python program to lowercase first n characters in a string.
uppercase= 'My Name is Mudasar Latif Memon'
l=uppercase.lower()
print (l)


# In[183]:


# Write a Python program to count and display the vowels of a given text.
text = 'My Name is Mudasar Latif Memon'
count=0
for i in text:
    if i == 'a':
        count= count+1
    elif i== 'e':
        count= count+1
    elif i== 'i':
        count= count+1
    elif  i== 'o':
        count= count+1
    elif i== 'u':
        count= count+1
print (count)


# In[201]:


# Write a Python program to remove the characters which have odd index values of a given string.
text = 'My Name is Mudasar Latif Memon'
y= text[ : : 2]
print (y)


# In[ ]:




