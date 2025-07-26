class pair_elements():
    def twoSum(self,nums,target):
        lookup = {}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],i)
            lookup[num] = i
        return None
value = int(input("Enter the number u want to search"))
result = pair_elements().twoSum([10,20,30,40,50,60,70],value)
if result:
    print("Index1 = %d,Index2 = %d"%(result[0],result[1]))
else:
    print("No pair found")