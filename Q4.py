n=int(input("Enter n: "))
def subtract(n):
    sum=0
    product=1
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n!=0:
        rem=n%10
        sum=sum+rem
        product=product*rem
        n=n//10
    return (sign*product)-(sign*sum)

print(subtract(n))