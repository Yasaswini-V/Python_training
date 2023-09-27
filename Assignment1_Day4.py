def sum(*numbers):
    result=0
    for number in numbers:
        result+=number
    return result

def average(*args):
    return sum(*args)/len(args)

average(1,2,3)