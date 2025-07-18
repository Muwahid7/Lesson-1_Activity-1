numbers = (4,3,2,2,-1,18)
numbers_2 = (2,4,8,8,3,2,9)
result = tuple(x*y for x,y in zip(numbers,numbers_2))
print(result)