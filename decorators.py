
def div(x,y):
    c=x/y
    return c

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


a=smart_div(div)
print(a(2,8))