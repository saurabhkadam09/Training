a=1
def fact(n):
    global a
    for i in range(1,n+1):
        b=a*i
        a=b
    return b


result=fact(6)
print(result)

def rec_fact(n):
    if n==0:
        return 1
    return n*rec_fact(n-1)

result=rec_fact(5)
print(result)