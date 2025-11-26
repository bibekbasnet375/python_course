def bibek():
    print("hii it's me bibek")


bibek()
bibek()

# parameters and arguments
def sport(name="ronaldo", khel="football"): #here name and khel are the parameters
    print( name + " like " +khel)
    print("Welcome")

print("hii")
sport("bibek","football") #bibek and football are the arguments
sport("bijay","cricket")
print("thank you")
sport()

#mixing positional and keyword arguments
def food(name, taste, color):
    print(name, "is", taste, "and looks", color, "in color")

food("apple",color="red",taste="good")

#passing different data types
def my_function(person):
    print("name:",person["nam"])
    print("age:",person["ag"])
    print("class:",person["class"])

my_stat= {"nam": "bibek", "ag": 24, "class":17}
my_prof= {"nam":"bijay", "ag": 29, "class": 20}
my_function(my_stat)
my_function(my_prof)

#return values
def multiple_table():
    x=1
    y=5
    while x < 11:
        result = x * y
        print(result)
        x = x + 1

multiple_table()

    


