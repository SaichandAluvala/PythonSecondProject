class A:

 def test1(self):
    print(" method named test1 of A called ")

class B(A):

 def test10(self):
    print(" method named test1 of B called ")

class C(B,A):

 def testa(self):
    print(" method named test1 of C called ")
    print("Test")
 def test2(self):
    print("method named test2 of C called")

object=C()
object.test1() #

"""
class D(B,C):

 def test2(self):
    print(" method named test2 of D called ")


object1=D()

It will call the test1 of D but there is not test1 function move to (B,C)>>B has test1--
It will be print out 

object1.test1() #method named test1 of c called  Test
"""



