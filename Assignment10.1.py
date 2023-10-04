
class prime_range:
    def __init__(self, end,start=0):
        if start==0:
            self.current = start
            self.end = end
        elif start>end:
            self.current=end
            self.end=start

    def __iter__(self):
        return self

    def is_prime(self,n):
        if n<=1:
            return False
        test=2
        while test<n:
            if n%test==0:
                return False
            test+=1
        return True

    def __next__(self):
        while self.current< self.end:
            num=self.current
            self.current+=1
            if self.is_prime(num):
                return num
        raise StopIteration

def main():
    print("------use case 1-------")
    for num in prime_range(10):
            print(num)
    print("------use case 2--------")
    try:
        primes= prime_range(10,20)
        it=iter(primes)
        print(next(it)) #11
        print(next(it)) #13
        print(next(it)) #17
        print(next(it)) #19
        print(next(it)) 
    except StopIteration:
        print(" ")

main()