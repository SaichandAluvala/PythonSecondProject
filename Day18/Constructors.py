#Constructors
#Constructors are 2 types 1. Default 2. Parameterized Constructor
# __init__(self) is Default
# __init__(self, name, age) is Parameterized Constructor
class constructorclass:
    def __init__(self, name, age):
        self.name = name
        self.age=age

    def getvalue(self):
        print("name of the person is ", self.name, ", age is ", self.age)

#name=input("Enter your name")
#age=input("Enter your age")
cs=constructorclass("Saichand",30)
cs.getvalue()