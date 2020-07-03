from  numpy import *

a=ones(2,int)
b=linspace(2,10,5)  #To divide 2-10 in 5 parts
c=logspace(2,10,5)  #To divide 2-10 in 5 parts as log
print(a,b,c)

m1=matrix('1,3;3,5')
m2=matrix('2,4;4,6')
m3=m1.flatten()
sum=m1+m2
mul=m1*m2
print(m3)
print(m1)
print(m2)
print(sum)
print(mul)