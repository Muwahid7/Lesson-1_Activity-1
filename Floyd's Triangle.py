Rows = int(input("Enter the number of rows"))
num = 1
print("Floyd's Triangle")
for i in range(1,Rows+1):
    for j in range(1,i+1):
        print(num,end='')
        num=num+1
    print()