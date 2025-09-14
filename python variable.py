#python variable
#creating variables
x= 5
print(x)
y= "bibek"
print(y)
x= "basnet"
print(x)

#casting
x= str(5)
y= int(5)
z= float(5)
print(x)
print(y)
print(z)

#get the type
x= 5.0
y= "bibek"

print(type(x))
print(type(y))

#case sensative
a= 6
A= "cat"
print(a)
print(A)

#variable names
best_footballer= "Ronaldo"
_best_footballer= "ronaldo"
Bestfootballplayer = "ronaldo"
print("best_footballer")

#illegal variable names
#1bestfootballer= "messi"
#best-footballer= "messi"
#best footballer= "messi"

#many values to multiple variables
x,y,z ="cat","dog","cow"
print(x)
print(y)
print(z)
z= "rat"
print(x,y,z)

#one value to many variables
x=y=z= "basnet"
print(x)
print(y)

#unpack a collection
sports= ["football","cricket","volleyball"]
a,b,c = sports
print(a)
print(b)

#output variables
x= "my "
y="name is "
z= "bibek"
print(x,y,z)
print(x+y+z)
x=10
y=23
print(x+y)
x=7
y= "ronaldo"
print(x,y)
print("hello","world")

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#x is outside the function and used inside also
x= "beautiful"

def mylady():
  x= "preety"
  print("She is " + x)

mylady()
print("she is " + x)

#global keyword
x= "beautiful"

def mylady():
  global x
  x= "preety"
  print("She is " + x)

mylady()
print("she is " + x)

x= list(("apple","orange","pineapple"))
print(x)
x=tuple(("cat","dog","rat"))
print(x)
x= dict(name="bibek",age=24, level="bachelor")
print(x)
#python numbers
x= 1
y= 5.6
z= 4j
a= float(x)
b= complex(y)
c= int(y)
print(a)
print(b)
print(c)
#random number
import random
print(random.randrange(20,80))

#exercise
weight = int(input("what is your weight in gram?"))
weight = weight/1000
print("weight in kg= " , weight)