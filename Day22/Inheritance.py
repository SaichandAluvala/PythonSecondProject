#Inheritance is OOPS --Take variables, Fuctions from Parent class to Child class

"""
 Inheritance 3 types 1) Single Inheritance  x>>z
                     2) Multiple Inheritance  x,y>>z
                     3) Multi (GrandParent) Inheritance x>>y>>z
                     4) Hierarchical Inheritance  x>>z,z1,z2
                     5) Hybrid Inheritance  x,y>>z>>z1>>z2

"""
class parentclass():
    def walk(self):
        print("walking")
    def dance(self):
        print("dance")


class childclass(parentclass):
    def read(self):
        print("reading")


cc=childclass()
cc.read()
cc.walk()
cc.dance()



