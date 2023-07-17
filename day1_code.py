
# Printing Welcome

name= input ()
print ("Welcome Mr. "+ name)


# Calculating  Gross Pay

hours = int(input ("enter the hours "))
rateperhour = int(input ("enter rate per hour "))
grosspay= hours*rateperhour
print ("your grosspay is", grosspay)

# Celcius to Farhenheit Temprature Conversion

celcius= input ("enter the celcius temprature")

celcius= int (input ("enter the celcius temprature"))
farhenheit= (celcius * 9/5) + 32
print ("The Farhenheit Temprature is =", farhenheit ,"F")


# Concatenation

first_name= input ('Enter your first Name')
last_name= input ('Enter your last Name')
complete_name= first_name +" "+ last_name 
print ('Your compelete Name is', complete_name)



## Expressions ##

5==5

x= 2
y= 3
x==y

# Logical Operators

x!=y

# Boolean Operators

x is y
x and y
x>0 and x<10


not (x>y)

not (x<y)

x= int (input ('input an integer '))
if x <10:
    print ('x is less than 10')

# Conditional Statements if elif

x=10
y=10
if x<y:
    print ('x is less than y')
elif x>y:
    print ('x is greated than y')
else:
    print ('x and y are equal')


# conditional Nested if else
x=10
y=10
if x==y:
    print ('x and y are equal')
else :
        if x<y:
        print ('x is less than y')
            else:
                print ('x and y is greated')


# Try Except


inp = input ('Enter Farhenheit Temprature:')
try:
    far = float (inp)
    cel = (far- 32.0) * 5.0 /9.0 
    print(cel)
except:
    print ('Please enter a number')


# Nest if elif 


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


# Import Library Math


import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# Import library with Alias


import math as ma
degrees = 45
radians = degrees / 360.0 * 2 * ma.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# Import specific function from library


from math import pi,sin
degrees = 45
radians = degrees / 360.0 * 2 * ma.pi

rad_sin= math.sin (radians)
print (radians)
print (rad_sin)


# Random function/ randint/ randchoice


import random
for i in range (10):
    x= random.randint(5,10)
    print (x)

print (x)


t= ['Mudasar', 'Latif', 'Memon']
random.choice(t)


def print_fullname(first_name, last_name)
print (first_name)
print (last_name)

print_fullname()



def print_fullname(first_name, last_name)
print (first_name)
print (last_name)

# Function without return

def print_fullname(first_name, last_name):
print (first_name)
print (last_name)


# Return

def print_fullname(first_name, last_name):
    print (first_name)
    print (last_name)

    return (first_name, last_name)
print_fullname('Mudasar', 'Latif')


# End of First Day




