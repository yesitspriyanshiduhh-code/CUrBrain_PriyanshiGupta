n = int(input("Enter number of terms: "))
arr = []

for i in range(n):
    val = int(input("Enter number of terms: "))
    arr.append(val)

mod = int(input("Enter modulo value: "))
prefix = 0

for i in range(n):
    prefix += arr[i]

    if prefix % abs(mod) == 0:
        print("True")
        break
else:
    print("False")
