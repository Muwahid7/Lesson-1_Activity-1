x=5
if(type(x)is int):
    print("true")
else:
    print("False")
y=0.8
if(type(y)is float):
    print("true")
else:
    print("False")
a=3
b=3
if(a is b):
    print("a and b have same identity")
b=67
if(a is not b):
    print("a and b have different identity")