mod = 1000000007
result = 0

n = int(input("Enter number of terms in array: "))

for i in range(n):
    val = int(input("Enter value: "))
    result = (result + val) % mod

print("result:", result)
