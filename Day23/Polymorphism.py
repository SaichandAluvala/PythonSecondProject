#Polymorphism means many ways to actions
"""
there are 2 types in Polymorphism
  1. Overriding  (Methods=Methods & Parameters=Parameters) - Runtime Polymporpism
  2. Overloading (Methods=Methods ) - Compile Polymorphism

  Base class-- Parent class
  Inherated class -- Child class
  Derived class -- Main class


  ** super() means below:
class A
     def function1(self)
      print("A)
class B(A)
    def function2(self)
    print("B")
    def function1(self)
    print("B2)"


obj =B()
obj.function1() //B2
obj.super().function1() //A
"""