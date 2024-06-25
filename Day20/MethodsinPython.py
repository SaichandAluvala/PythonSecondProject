#Methods or Functions are same in python

"""
2 types of methods 1) Class or Static Methods
                2) Instance methods

"""
class methods:
    def __init__(self):
        self.name="Haneesh"
        self.age=2

    @staticmethod  #after @anything is Decorate
    def hello():
        print("Hello World!")

    def callvalues(self):
        print("name is ",self.name,"and age is ",self.age)


m=methods()
#m.name="Saichand"
#m.age=30
m.callvalues()
m.hello()

m2=methods()
m2.name="Saichand"
m2.age=30
m2.callvalues()
m2.hello()