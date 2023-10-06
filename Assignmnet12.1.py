import time

def cache(fn):
    result=dict()
    def inner(*args):
        start=time.time()
        if args[0] in result.keys():
            value=result[args[0]]
            print("Cache value")
        else:
            num,value=(fn(*args))
            result[num]=value
            print("Uncached value")
        end=time.time()
        time_taken=end-start
        inner.time_taken=time_taken
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
print(factorial.time_taken)
print("----------------")
x=factorial(7)
print(x)
print(factorial.time_taken)
print("-------------------")
x=factorial(5)
print(x)
print(factorial.time_taken)