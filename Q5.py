list=[]
n=int(input("Enter the integer: "))
while(n!=0):
    rem=n%10
    if(rem%2==0):
        list.append(0)
    else:
        list.append(rem)
    n=n//10
print(list[::-1])