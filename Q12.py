base = int(input("enter base: "))
power = int(input("Enter power: "))
mod = int(input("Enter MODULO: "))

result = 1 % mod

for i in range(power):
    result = (result * base) % mod

print("Answer:", result)
