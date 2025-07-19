number_1 = [23,26,20,10]
number_2 = [16,21,11,40]
result = map(lambda x,y:x+y,number_1,number_2)
print("Addition of two lists")
print(list(result))
num_1 = [23,26,20,10]
def sq(n):
    return n*n
square = list(map(sq,num_1))
print("Square of numbers in list",square)