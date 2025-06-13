Range_1 = int(input("Enter a Number"))
Range_2 = int(input("Enter the second Number"))
print("prime numbers between",Range_1,Range_2)
for num in range(Range_1,Range_2+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print("These are the prime numbers",num)                                                                                                                            