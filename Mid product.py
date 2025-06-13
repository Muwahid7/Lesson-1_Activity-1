A = int(input("Enter a Number"))
T = A
numlen = 0
while T>0:
    numlen=numlen+1
    T=int(T/10)
if numlen>=4:
    numlen=int(numlen/2)
    chk=0
    while A>0:
        rem=A%10
        if chk==numlen:
            midone=rem
        elif chk==(numlen-1):
            midtwo=rem
        A=int(A/10)
        chk=chk+1
    Product = midone*midtwo
    print("The product of mid Digits is",Product)
else:
    print("It is not 4 digit of more than 4 digits number")