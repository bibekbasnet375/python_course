#python if..else
a= 55
f= 70
if f>a :
    print("f is greater than a")
if f>a : print("f is greater than a")

#elif condition
a=5
b=7
if b == a :
    print("b is equal to a")
elif b>a :
    print("b is greater than a")

#Else condition
b= 35
c= 40
if b>c:
    print("b is greater than c")
elif b==c:
    print("b is equal to c")
else:
    print("c is greater than b")

#short hand if...else
c=80
d=10
print("d") if d>c  else print("c")
print("d") if d>c else print("=") if c==d else print("c") #3 conditions

#and_or
e= 50
if c>d and c>e:
    print("c is the greatest value")
if c>d or c==d:
    print("c is greater than or equal to d")

#not
if not d>c:
    print("d is not greater than c")

#elif
is_hot= False
is_cold= True
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")

is_credit= False
cr= 100000
if is_credit:
     cr= 0.1 * int(cr)
     print("downpayment is ", cr)
else:
     cr= 0.2 * cr
     print("downpayment is", cr)

#nested if
x= 8
if x>10:
    print("x is greater than 10")
    if x>20:
        print("x is also greater than 20")
    else :
        print("but not above 20")
else:
    print("x is less than 10")





