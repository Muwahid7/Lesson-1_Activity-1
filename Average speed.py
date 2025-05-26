A=int(input("Enter the speed"))
B=int(input("Enter the speed"))
c=int(input("Enter the speed"))
Average=(A+B+c)/3
print(Average)
if Average>A and Average>B and Average>c:
    print(Average,A,B,c)
elif Average>A and Average>B:
    print(Average,A,B)
elif Average>A and Average>c:
    print(Average,A,c)
elif Average>B and Average>c:
    print(Average,B,c)
elif Average>A:
    print(Average,A)
elif Average>B:
    print(Average,B)
elif Average>c:
    print(Average,c)
else:
    print("Invalid")
