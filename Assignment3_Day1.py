def is_primes(number):
    if number<=1:
        return False
    test=2
    while test<number:
        if number%test==0:
            return False
        test+=1
    return True

def find_primes(min,max):
    count=min
    while count<max:
        if is_primes(count):
            print(count)
        count+=1


min=int(input("Enter a min value: "))
max=int(input("Enter  a max value: "))
find_primes(min,max)