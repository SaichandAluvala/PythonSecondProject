class A:
    def test1(self):
        print("method named test1 of A called")


class B(A):
    def test1(self):
        print("method named test1 of B called")
        super().test1()


class C(A):
    def test1(self):
        print("method named test1 of C called")
        #super().test1()


class D(B,C):
    def test2(self):
        print("method named test2 of D called")


object1 = D()
object1.test1() # method named test1 of B called method named test1 of A called