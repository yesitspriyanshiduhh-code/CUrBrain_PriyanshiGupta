n = int(input("Enter number of terms: "))
arr = []

for i in range(n):
    val = int(input("Enter value to insert: "))
    arr.append(val)

ans = arr[0]

for i in range(1, n):
    if abs(ans) > abs(arr[i]):
        ans = arr[i]

print("result:", ans)
