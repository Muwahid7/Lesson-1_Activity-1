Valid=False
while not Valid:
    try:
        n=int(input("Enter a number"))
        while n%2==0:
            print("Bye")
            Valid=True
    except ValueError:
        print("Invalid")    