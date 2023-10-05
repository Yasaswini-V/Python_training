import time

class Timer:
    def __enter__(self):
        self.start=time.time()
        return self

    def __exit__(self,t,e,s):
        self.end=time.time()
        self.time_taken=self.end-self.start
        return self.time_taken

def find_primes(min,max):
    values=[]
    for num in range(min,max+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                values.append(num)
    return values

with Timer() as t:  # t = Timer().__enter__()
    p=find_primes(2,20000)
    print('total primes', len(p))

# t.__exit__(t,e,s)
print('total time taken', t.time_taken)