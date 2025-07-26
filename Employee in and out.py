class employee():
    def __init__(self):
        print("Employee craeted")
    def __del__(self):
        print("Destructor called")
def Create_obj():
    print("Making the object")
    obj = employee()
    print("Function end")
    return obj
print(f"Calling {Create_obj()} function")
obj = Create_obj
print("Program end")