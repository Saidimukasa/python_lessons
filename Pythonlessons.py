print("Hello ,world!");
#This is an output statement in python
print("Welcome to Python!");
Greetings="Hello!"; #This is how you declare a string variable
print(Greetings);
# This is a comment
x=10  #this is how to declare a variable"
#This is a multi-line Comment!!
############################################
#Casting this enables you to declare a variable with a specific data type
x=int(3) #This is how to declare an integer variable
y=float(3.0) #This is how to declare a float variable
z=str("3") #This is how to declare a string variable
k=bool(3) #This is how to declare a boolean variable
l=complex(3j) #This is how to declare a complex variable
j=bytes(3) #This is how to declare a byte variable
#Getting the type of a variable
print(type(z)) #This is how to get the type of a variable
#Assigning multiple values to multiple variables
a,b,c=1,2,3#This is how to assign multiple values to multiple variables
print(a,b,c);#This is how to print multiple variables
#This will output the results in a single line or in a single row
#OR
#This will out the results vertically
print(a);
print(b);
print(c);
#Global variables- These are functions that are declared outside a function
#Local variables- These are functions that are declared inside a function
x = "awesome"

def myfunc():
  print("Python is " + x)#This is how to print a global variable

myfunc()
#Note:You can also create a global variable inside a function by using the global keyword
# def myfunc():
#       global K #This is how to create a global variable inside a function by using the global keyword
#         K="Awesome"

# myfunc()

# print("Python is " + k)

#Data types
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#Getting the data type of a variable
# x = 5
# print(type(x))
# x = "Hello World"
# print(type(x))
x="Hello World"
x=str("Hello World")#This is how to declare a string variable
print(x);
x=int(20)#This is how to declare an integer variable
print(x)
x=float(20.5)#This is how to declare a float variable
print(x)
x=complex(1j)#This is how to declare a complex variable
print(x)
x=list(("apple","banana","cherry"))#This is how to declare a list variable
print(x)
x=tuple(("apple","banana","cherry"))#This is how to declare a tuple variable
print(x);
x=range(6)#This is how to declare a range variable
print(x)
x=dict(name="John",age=36)#This is how to declare a dictionary variable
print(x)
x=set(("apple","banana","cherry"))#This is how to declare a set variable
print(x)
x=frozenset(("apple","banana","cherry"))#This is how to declare a frozenset variable
print(x)
x=bool(5)#This is how to declare a boolean variable
x=bytes(5)#This is how to declare a byte variable

######################################################
#Setting the Specific Data Type
# x = str("Hello World")#This is how to declare a string variable
# print(x);
# x = int(20)#This is how to declare an integer variable
# print(x)
#x = float(20.5)#This is how to declare a float variable
# print(x)
# x = complex(1j)#This is how to declare a complex variable
# print(x)
# x = list(("apple","banana","cherry"))#This is how to declare a list variable
# print(x)
# x = tuple(("apple","banana","cherry"))#This is how to declare a tuple variable
# print(x);
# x = range(6)#This is how to declare a range variable
# print(x)
# x = dict(name="John",age=36)#This is how to declare a dictionary variable
# print(x)
# x = set(("apple","banana","cherry"))#This is how to declare a set variable
# print(x)
# x = frozenset(("apple","banana","cherry"))#This is how to declare a frozenset variable
# print(x)
# x = bool(5)#This is how to declare a boolean variable
# x = bytes(5)#This is how to declare a byte variable

############################################
#Type Conversion
x=1#This is an integer
z=float(x)#This is how to convert an integer to a float
print(z)
#This is how to convert a float to an integer
a=1.5#This is a float
b=int(a);#This is how to convert a float to an integer
print(b)
#This is how to convert an integer to a string
A=1#This is an integer
B=str(A)#This is how to convert an integer to a string
print(B,"is a string")
""" my name is """ #This is a multiline string


##############################
#strings-hese are sorrounded by double or Single Quotes
name="John"
#This is how to access a single letter from an array using the Array notation name[1];
print(name[1])#This is how to print a specific character in a string
#Looping Through a String
for name in "john":#This is a for x(Variable) in y(word to be looped thru.) loop that is used to loop through a string
     print(name) #This is how to loop through a string
     ###################################
     #finding the length of a string
     NAME="John"
     print(len(NAME))#This is how to find the length of a string
     ##############################
     #Check phrase or character in a string
     greetings="Hello,world!"
     if "world" in greetings:
         print("Yes,'world' is present in the greetings")#This is how to check if a phrase or character is present in a string
         #Or 
         print("Hello,world!" in greetings)#This is how to check if a phrase or character is present in a string this is in form of a boolean
         
         
         
###Modifying Strings
State="I love Python"
print(State.upper())#This is how to convert a string to uppercase
print(State.lower())#This is how to convert a string to lowercase

###########
#replace
greetings="Hello,world!"
print(greetings.replace("H","g"))#This is how to replace a character in a string
#H is the word in the String to be changed with g
###########
#Split this is how to split a string into a list
greetings="Hello,world!"
print(greetings.split(","))#This is how to split a string into a list
print(greetings[1]);#This is how to print a specific character in a string

###############################
#String Concatenation-This is how to join two strings
a="Hello"
b="World"
c=a+b #This is how to join two strings but there is no space between the two strings
print(c)

# 2. String Concatenation-This is how to join two strings
a="Hello"
b="World"
c=a+" "+b #This is how to join two strings with a space between the two strings     
print(c) 
###############
#Escape Character


print("Hello,world!\n")#This is how to print a string
print("Hello,world!\t")#This is how to print a string with a tab

#############
#Lists-These are sorrounded by square brackets
#Thse are used to store multiple values in a single variable
#Example of a list of fruits  

mylist=["apple","banana","cherry"]
print(mylist);#This is how to access the Components in a list
#How to access a specific item in a list
print(mylist[1])#This is how to access a specific item in a list
print(mylist[-1])#This starts from the end of the list
# You can also the list() constructor to make a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
###############
#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#This is how to access a range of indexes
print(thislist[:4])#This accesses elements but stopps before the specified index meaning it does not include the specified index
print(thislist[2:])#Starts from the specified index and goes to the end of the list

#######################
#CHECK IF ITEM EXISTS IN A LIST
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: #We can use the in keyword to check if an item exists in a list
  print("Yes, 'apple' is in the fruits list")    
  
  
############################  
#Conditional Statements -if,elif,else
# age=30
# if age>10: #This is how to use an if statement but this requires an indentation
#     print("You are a teenager");
# elif age>20:#This is how to use an elif statement but this requires an indentation
#     print("You are an adult");
# else:#This is how to use an else statement but this requires an indentation
#     print("You are a child");
#  a=20 b=30 
    # if a>b: print("a is greater than b")#This is how to use a short hand if statement    
 
 #Loops
 
 
#While loop: With the while loop we can execute a set of statements as long as a condition is true. 
#Example
# int num=0
i = 1 #This is how to declare a variable
while i < 6:#This is the Condition once the condition is false the loop stops thus if it is Correct the loop will continue
  print(i)
  i += 1 #This is how to increment a variable once you don't Increment the loop will be an infinite loop
  
  #we can also use the break statement to stop the loop even if the while condition is true
  while i<6:
      print(i)
      if i==3:
          break
      i+=1
#we can also use the continue statement to stop the current iteration and continue with the next
    
      # while i<6:
      #     print(i)
      # if i==3:
      #     continue
      # i+=1  
#For-Loops
#Example
  #A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
  fruits = ["apple", "banana", "cherry"]
for x in fruits: #The for x in Y is used to loop thru an array ,set tuple or Dictionary among others
  print(x)

#BREAK STATEMENT IN A FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":#This is how to use the break statement in a for loop
    break  
  
  #CONTINUE STATEMENT IN A FOR LOOP
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":#This enables a loop to move on once the Condition is met
    continue
  print(x)
#RANGE FUNCTION-This returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.in the Range function the first number is the starting number and the second number is the ending number
for x in range(10):#This is how to use the range function
  print(x)#This prints the numbers from 0 to 9 there is no 10 in the Sequence
  #We can also specify the starting and ending number since by default the starting number is 0
for y in range(2, 6):#This is how to specify the starting and ending number
# print(y)

######################################################
#Else-In a for loop we can use the else statement to specify a block of code to be executed when the loop is finished
 for x in range(6):
  print(x)
 else:
   print("Finally finished!")#This is how to use the else statement in a for loop
   #But this will be executed only if the loop is not stopped by a break statement
   for x in range(6):
      if x == 3: break
  # print(x)#This is how to use the break statement in a for loop
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

#Nested Loops-A nested loop is a loop inside a loop.
#You can also Fix more and more loops inside each other
#And this is known  as Looping inside a loop
#Example
adj = ["red", "big", "tasty"]
fruits=['apple','banana','cherry']
for x in adj:
  for y in fruits:
    print(x,y);
    
###########
# Functions- A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
#Creating a function in python
def my_function():#This is how to create a function
  print("Hello from a function")

#Calling a function
my_function()#This is how to call a function
#The function has arguments that can be passed to it and it can also return a value
#The term Args or Arguments can be used interchangeably
def my_function(fname):#This is how to create a function with a parameter
      print(fname + " Peters")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("John")
 #You can use the Return statement to return a value from a function
 
def Summation(x):
        return 5+x;
      #When one uses the return statement the function stops executing and returns the value they are supposed to print it out 
# Summation(3);
print("The summation is",Summation(3));

#ARRAYS-this is like a list but it is a fixed size and it can only hold a single data type ,this is used to store multiple values in a single variable
#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#Therefore to use Arrays in python we need to import a library called NumPy
 #syntax
cars = ["Ford", "Volvo", "BMW"] #This is how to create an array
print(cars[0])#This is how to access an element in an array ,this uses the Index Notation to access the element and these are Zero based meaning the first element is at index 0 
#Checking the length of an array
print(len(cars))#This is how to check the length of an array
#lOOPING THROUGH AN ARRAY

for x in cars:
  print(x);#This wil output all the elements in the array
  
#Checking if an element exists in an array-basically we use the in keyword to check if an element exists in an array
if "Fod" in cars:
  print("Yes, 'Ford' is in the cars list")#This is how to check if an element exists in an array
else:
    print("No, 'Ford' is not in the cars list")  
    
#Adding an element to an array 
#Here we use the Append method to add an element to an array eg cars.append("Toyota")
#To add an element to the end of the array, use the append() method.
cars.append("Honda")#This is how to add an element to an array  
print(cars)#This is how to print an array

#removing an element from an array using the pop method eg cars.pop(1)
#For this case you can either use the pop method or the remove method they both work the same way
#For the case of pop we can also use the remove method eg cars.remove("Volvo")
cars.pop(1)#This is how to remove an element from an array
print(cars)
cars.remove("Volvo")#This is how to remove an element from an array
#For the case of remove we use the exact name of the element to remove it from the array not the index

#CLASSES/OBJECTS
#A Class is like an object constructor, or a "blueprint" for creating objects.
#To create a class, use the keyword class:
class myClass:#This is how to create a class in python
  x=3;
#Creating an object
#Now we can use the class named myClass to create objects:
#Create an object named p1, and print the value of x:
p1=myClass();
print(p1.x)#This is how to create an object in python