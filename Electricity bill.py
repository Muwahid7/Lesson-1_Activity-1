Units = int(input("How many units consumed?"))
if(Units < 50):
    Amount = Units*2.60
    Tax = 25
elif(Units <= 100):
    Amount = Units*3.25
    Tax = 35
elif(Units <= 200):
    Amount = Units*5.26
    Tax = 45
else:
    Amount = Units*8.45
    Tax = 75
Total = Amount+Tax
print(Total)