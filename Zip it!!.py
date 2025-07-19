num_1 = {23,26,10}
num_2 = {20,4,16,11}
num_3 = list(zip(num_1,num_2))
print("zipped list from two lists",num_3)
number_1 = [23,26,10,16]
number_2 = [20,4,16,11]
for x,y in zip(number_1,number_2[::-1]):
    print(x,y)
name = ['samay','damodar','manjulika']
age = [15,21,34,54]
new_dict = {name:age for name,age in zip(name,age)}
print('\n{}'.format(new_dict))