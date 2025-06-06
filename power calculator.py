base = int(input("Enter a Number"))
Exponent = int(input("Enter a Number"))
result = 1
for _ in range(Exponent):
    result*=base
    print(result)
