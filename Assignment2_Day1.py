n=int(input("enter the total number of inputs "))

count=1
max1=int(input(f'number#{count}? '))
max2=None

while count<n:
    count+=1
    value=int(input(f'number#{count}? '))
    if value>max1:
        max2=max1
        max1=value
    elif value<max1 and value>max2:
        max2=value
print("The second largest is:",max2)