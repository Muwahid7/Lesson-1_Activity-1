def square_it_out(start,end):
    square_values = []
    for num in range(start,end+1):
        square = num*num
        if square%2!=0:
            square_values.append(square)
    print("odd square values",square_values)
start_num = int(input("Enter the start number"))
end_num = int(input("Enter the end number"))
square_it_out(start_num,end_num)
