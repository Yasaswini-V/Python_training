def frequency(list1):
    count=0
    dict1=dict()
    for i in list1:
        dict1[i]=list1.count(i)
    return dict1
               
n=int(input("Enter the number of inputs: "))
x=list()
for i in range(n):
    x.append(int(input("Enter the numbers: ")))
f=dict()
f=frequency(x)
print(f)