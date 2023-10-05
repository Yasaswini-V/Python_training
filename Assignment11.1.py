import time
def performance_log(fn):
    def inner(*args):
        start=time.time()
        result=fn(*args)
        end=time.time()
        print(f'The performance of {fn.__name__} is {end-start}')
        return result
    return inner


def is_prime(num):
    if num<=1:
        return False
    for x in range(2,num):
        if num%x==0:
            return False
    return True

@performance_log
def find_primes(min,max):
    result=[]
    for i in range(min,max):
        if is_prime(i):
            result.append(i)
    return result

x=find_primes(2,50000)
print(len(x))
