try:
    Num_1,Num_2=eval(input("Enter two numbers seperated by a comma"))
    Result=Num_1/Num_2
    print("Result is",Result)
except ZeroDivisionError:
    print("Division by 0 is Error")
except SyntaxError:
    print("Comma is Missing")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This code will execute no matter of any error")
    
    