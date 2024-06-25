#Access Modifiers in python

"""

3 types  1) Public -- no restriction
         2) Private -- full restriction
         3) Protected -- Partial restriction

         if no access modifier then it is " Public "


         name=public
         _name=protected
         __name=private
"""


class accessmodifier:
    def __init__(self,name,age):
        self.__name=name
        self.age=age


    def getvalue(self):
        print("name is ",self.__name,"age is ",self.age)


c=accessmodifier("Saichand",30)
c.getvalue()

