import time


def cache(fn):
    result=dict()
    def inner(*args):
        if args[0] in result.keys():
            value=result[args[0]]
            print("Cache value")
        else:
            num,value=(fn(*args))
            result[num]=value
            print("Uncached value")
        return value
    return inner
@cache
def factorial(n):
    fn=1
    for i in range(1,n+1):
        fn*=i
    return n,fn

x=factorial(5)
print(x)
print("----------------")
x=factorial(7)
print(x)
print("-------------------")
x=factorial(5)
print(x)