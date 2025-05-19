Actual_cost=float(input("Please enter the actual product price"))
Sale_amount=float(input("Please enter the sales amount"))
if(Sale_amount>Actual_cost):
    Amount=Sale_amount-Actual_cost
    print("Total profit={0}".format(Amount))
else:
    print("Loss")