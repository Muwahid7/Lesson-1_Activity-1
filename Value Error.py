try:
    Number=int(input("Enter an integer value"))
    print("The number entered is",Number)
except ValueError as EX:
    print("Exception",EX)
