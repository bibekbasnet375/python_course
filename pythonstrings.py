#string in python is surrounded by single or double quotation mark
print("hello, world")
print('hii')

#quotes inside quotes
print("it's our country nepal")
print("this is an 'apple'")
print('that is "not good"')

#multiline strings
a= """ I am a good guy
 I study well
 I am punctual too."""
print(a)

print(a[8]) #string are arrays
print(len(a)) #length of string
print("am" in a) #check string
print("ban" in a)
print("i" not in a)
print("I" not in a)

#python slicing string
print(a[8:15])
print(a[:12]) #slice from start
print(a[18:])#slice to end
print(a[-5:-1]) #negative indexing
f= "bibek basnet"
print(f[1:-1])

#modify string
b= "I like sports"
print(b.upper()) #must use . function to modify
print(b.lower())
print(b.replace("sports", 'football'))

#F-strings (format string)
a= 18
txt = f"my name is jack, i am {a} years old"
print(txt)
print(f"the price of shoes is {20*500}")









