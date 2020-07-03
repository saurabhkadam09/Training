
def sum(a,b):
    c=a+b
    print(c)

sum(10,20)

def update(a):                  #the arguments passed in the python are neither pass by value nor pass by reference
    print(id(a))
    a=8
    print(id(a))
    print(a)

x=10
update(x)
print(id(x))


def update(a):
    a[1]=8
    print(a)

x=[10,20,30]
update(x)
print(x)
print()


def add(*a):
    k=0
    for i in a:
        k=k+i
    print(k)
add(20,26,57)

def info(a,**b):
    print(a)
    for i,j in b.items():
         print(i,j)

info('saurabh',age=24,city='Mumbai')