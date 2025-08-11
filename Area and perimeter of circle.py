class circle:
    def __init__ (self,perimeter,area):
        R = int(input("Enter the radius"))
        self.perimeter = 2*3.14*R
        self.area = 3.14*(R**2)
obj = circle(0,0)
P = obj.perimeter
A = obj.area
print(P)
print(A)