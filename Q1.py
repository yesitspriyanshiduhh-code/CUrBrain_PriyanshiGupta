n=int(input("Enter the digits\n"))
def even(n):
    count=0
    n=abs(n)
    while(n!=0):
        rem=n%10
        count+=1
        n=n//10
    if(count%2==0):
        return True
    return False
print(even(n))