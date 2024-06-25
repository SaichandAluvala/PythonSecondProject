#Assignment for OOPS concepts
from ast import Str


class Person:
    def setvalue(self, name, age):
        self.name = name
        self.age=age


    def getvalue(self):
        print("The name of the person is ",self.name,"and the age is ",self.age)


p=Person()
p.setvalue("John",22)
p.getvalue()

p2=Person()
p2.setvalue("Jack",25)
p2.getvalue()