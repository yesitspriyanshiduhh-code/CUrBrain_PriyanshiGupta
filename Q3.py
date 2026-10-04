n=int(input("Enter n: "))
def palindromeOrSum(n):
    temp=n
    rev=0
    n=abs(n)
    sign = -1 if n < 0 else 1
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(temp<0):
         print(rev)
         return (-1*rev)+temp
    if(temp==rev):
        return True
    else:
        sum=rev+temp
        return sum
print(palindromeOrSum(n))   