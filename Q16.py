n = int(input("Enter number of terms: "))
arr = []

for i in range(n):
    val = int(input("Enter value to insert: "))
    arr.append(val)

first = 0
second = 0
hasFirst = False
hasSecond = False

for i in range(n):
    if not hasFirst or arr[i] > first:
        if hasFirst:
            second = first
            hasSecond = True

        first = arr[i]
        hasFirst = True

    elif arr[i] < first and (not hasSecond or arr[i] > second):
        second = arr[i]
        hasSecond = True

if hasSecond:
    print(second)
else:
    print(-1)
