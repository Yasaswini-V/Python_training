n=int(input("enter the total numbers: "))
count=1
max1=int(input(f'number#{count}? '))

while count<n:
    count+=1
    value=int(input(f'number#{count}? '))
    if value>max1:
        max1=value