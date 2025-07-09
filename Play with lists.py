list_1 = [23,10,26,16]
print(list_1)
count = 0
for i in list_1:
    count+=i
Average = count/len(list_1)
print("The sum is",count)
print("The average is",Average)
list_1.sort()
print("The smallest number is",list_1[0])
print("The largest number is",list_1[-1])