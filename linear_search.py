list=[2,15,23,34,49,58,66]

num=49

def sort(lst,n):
    for i in range(0,len(lst),1):
        if globals()['num']==lst[i]:
            return True

if sort(list,num):
    print("Found ")
else:
    print("Not Found")