n = int(input("Enter number of terms: "))
thershold = int(input("Enter thershold value: "))
original = []
ans = []

for i in range(n):
    val = int(input("Enter value to insert: "))
    original.append(val)

for i in range(n):
    if original[i] >= thershold:
        ans.append(original[i])

print(ans)
