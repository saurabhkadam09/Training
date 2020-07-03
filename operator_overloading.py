#as we know in python everything is a object, so to add two operands of student class (objects) we need to
#define a funtion to add these two objects of student class
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print(m1,m2)

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        return (m1,m2)

    def __str__(self):
        print('{} {}'.format(self.m1,self.m2))

saurabh=student(85,90)
dhiraj=student(80,85)
sum=student.__add__(saurabh,dhiraj)   #Addition operation defined in terms of function and object.
print(sum)
print(saurabh+dhiraj)
print(saurabh)