#python booleans : represents two values true or false
print(10 > 50)

#print message based on condition
a= 20
b= 30
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#bool values
print(bool("hello")) #true bool value
print(bool(15))
print(bool()) #false bool value
print(bool(""))

#python operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)# returns True because z is the same object as x

print(x is y)# returns False because x is not the same object as y, even if they have the same content

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
