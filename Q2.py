n=int(input("Enter n: "))
def reverse_and_double(n):
    rev=0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    temp=rev*2
    return sign*temp

print(reverse_and_double(n))