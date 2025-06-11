A = int(input("Enter a number"))
Sum = 0
Temp = A
while Temp>0:
    Digit = Temp%10
    Sum+=Digit**3
    Temp//=10
if A == Sum:
    print(A,"is an armstrong number")
else:
    print(A,"is not an armstrong number")