# WHILE loop

i= 1
while i<7 :
    print(i)
    i += 1

#break statement
i= 2
while i<5 :
    print(i)
    if i== 3:
        break
    i += 1

#continue statement
i= 1
while i<6 :
    i += 1
    if i== 3:
        continue
    print(i)

#else statement
i= 6 
while i> 1:
    print(i)
    i -= 1
else:
    print("i is no longer greater than 1")

# FOR loop

#print each item in the list 
fruits = ["apple", "banana", "orange"]
for x in fruits:
    print(x)

#print each item in a string
for x in "bibek":
    print(x)

#break in for loop
sports = ["football", "cricket","samosa", "golf"]
for x in sports:
    print(x)
    if x == "samosa":
     print("not any sports anymore")
     break

#continue in for loop
for x in sports:
    print(x)
    if x == "samosa":
        print("samosa is not the sport")
        continue
    
#range function in for loop
for x in range(6):
    print(x)

for x in range(2,8):
    print(x)

for x in range(1, 40, 3):
    print(x)

for x in range(5):
    print(x)
else:
    print("Finally finished!")

adj= ["big", "tasty", "small"]
fruits= [ "apple", "orange", "banana"]
for x in adj:
    for y in fruits:
        print(x,y)



