'''
# eg:3
def profile(name, age, place):
    txt ="my name is {}. iam{} years old. iam from{}."
    print(name, age, place)
profile("aid",20, "cbe")

# ! eg:;4
# ? function with return statement

def f1():
    z = 8
f1()
print(z) # error --> cannot use outside the fucnction


def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark(object):
    print(object+4)
gracemark()

def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palidrome")
    else:
        print("not palidrome")
a = int(input("enter the value: "))
palindrome(a)

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args

# * Positional args
# ? The position of parameter have to be same as position as arguments

def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

profile("malli",6300089837,100)

# Eg:-1
#? The position of parameter have to be same as position as argument

def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
profile(6300089837,"malli", 98) # unexpected output"


# * Keyword args
# ! Eg:-1
# To overcome the disadvantage of position args,we use keywords args
# It is the process of initialising the parameters with the args while calling the
# function

# degault args

Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

# ! eg:2
exception
def profile(name, phone,place="kadapa"): # error --> coz default args should not follow # positional param
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
        txt = "my name is {}. My phone number is {}. i am from{}."
        print(txt.format(name, phone, place))
    else:
            print("you are not eligible to signup")
file("malli", 6300089837)
         
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
        txt="My name is{}. My phone number{}. I got{} marks{}."
        print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
profile("malli",6300089837)

# ! eg:2
def profile(*name, age):
    for val in name:
        print("my name is ", val, "my age is", age)
profile("malli", 'name2', 'name3', 23) # error ---> age has no args

def profile(age, *name):
    for val in name:
        print("my name is", val, "my age is", age)
        profile(23, "malli", 'name2', 'name3')

# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation                            

# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1

def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    

# Eg:-2

# create of a method
# when the function is created with a class is called as method

class person:
    def display(person):
        print("hello welcome to class")

p = person()
p.display()

# ? eg:3
# ! method with parameter
class person:
    def display(person, name, age):
        print(name, age)

p = person()
p.display("malli", 23)

# ? eg:4
class person1:
    frame = "malli" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()

class person1:
    fname = "Asif" # attribute or static variable
    lname = "T"

    def first_name(person
# def first_name(person):
        print(person.fname)

    def full_name(person):
        print(person.fname+" " +person.lname)

p = person1()
p.first_name()
p.full_name()

#! Eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation

class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught th
'''



























