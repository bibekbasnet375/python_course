#create class 
class MyClass:
    x= 5

print(MyClass)

#create objects
class MyClass:
    x= 7

p1= MyClass
print(p1.x)

#creating class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

#creating object
p1= Person("bibek",24, "lasune")
p2= Person("ram", 30, "ktm")

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p1.address)
print(p2.address)

class Upaya:
    def __init__(vendor, name, address, pan):
        vendor.name = name
        vendor.address = address
        vendor.pan = pan

v1= Upaya("bijay", "boudha", 123)
v2= Upaya("jenii", "pepsi", 345)
v3= Upaya("ashmina", "pharping", 456)

print(v1.name)
print(v1.address)
print(v1.pan)
        
