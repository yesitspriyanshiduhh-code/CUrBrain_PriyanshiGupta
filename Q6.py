N = int(input("Enter N: "))
A = int(input("Enter digit A: "))
B = int(input("Enter digit B: "))

count_A = 0
count_B = 0

while N > 0:
    digit = N % 10

    if digit == A:
        count_A += 1
    if digit == B:
        count_B += 1

    N //= 10

print(abs(count_A - count_B))