import array as arr
array_num = arr.array('i',[1,3,5,3,7,9,3])
print("This is the original array",array_num)
print("Number of occurrences of number 3 in array",(array_num.count(3)))
array_num.reverse()
print("reverse order of array",(array_num))