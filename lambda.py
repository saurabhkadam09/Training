from sys import *
from functools import reduce
y=lambda a:a*a

print(y(25))

lst=[2,5,6,8,11,13,16,18]
list1 = list(filter(lambda a:a%2==0,lst))
doubles=list(map(lambda a:a*a,lst))
red=reduce(lambda a,b:a+b, lst)

print(list1)
print(doubles)
print(red)