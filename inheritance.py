
class A:
    def __init__(self):
        print("Init A")
    def feature1(self):
        print("This is feature 1")
    def feature2(self):
        print("This is feature 2")
class B:
    def __init__(self):
        print("Init B")
    def feature3(self):
        print("This is feature 3")
    def feature4(self):
        print("This is feature 4")

class C(A,B):                          #This is a multiple inheritance
    def feature5(self):
        print("This is feature 5")

a=A()
b=B()
c=C()
a.feature1()
a.feature2()
c.feature4()