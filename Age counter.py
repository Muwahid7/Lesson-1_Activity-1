try:
    Age=int(input("Enter your Age"))
    if Age<=0 or Age>150:
        print("Invalid age entered")
    else:
        print("Age is valid")
        if Age%2==0:
            print("Your age is even")
        else:
            print("Your age is odd")
finally:
    print("Age is not valid")
