#a=[10,20,30,40]
#itr=iter(a)
#print(itr.__next__())

class repeat:

    def __init__(self,m):
        self.k=1


    def __iter__(self):
        return self

    def __next__(self):
        val=self.k
        self.k=self.k+1
        return val

b=[11,22,33,44]
itr2=repeat(b)
print(itr2.__next__())