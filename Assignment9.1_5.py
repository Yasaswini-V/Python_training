#Bubble sorting
def sorting(s):
    print("The list before sorting:",s)
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if s[j]>=s[j+1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
    print("The sorted list is:",s)

def main():
    list1=[7,3,5,1,0,2]
    list2=[99,55,1,9,2,4,0,78]
    sorting(list1)
    sorting(list2)

main()