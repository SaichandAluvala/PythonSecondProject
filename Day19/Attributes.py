#Attributes

"""
Variables can be Datamembers, Parameters, Attributes, or Properities

2 types of Attributes: 1) Class Attributes
                       2) Instance Attributes

                       """

class Person1:
    city="Hyderabad" #class Attribute or Variable
    def __init__(self): #age, name are Instance Attributes or Varialbe
        self.name = "Saicahdn"
        self.age=30

    def getvalue(self):
        print("Name of the person is ",self.name,"age of the persion is ",self.age, "the city is ",Person1.city)

#p1=Person1("Saichand",30)
p1=Person1()
p1.name="newSaichand" #output is newSaichand and 300
p1.age=300
p1.getvalue()

#p2=Person1("Saichand1",3)
#p2.getvalue()
