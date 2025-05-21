Height = float(input("enter your height in centimeters"))
Weight = float(input("enter your weight in kilograms"))
BMI = Weight/(Height/100)**2
print("Your BMI is",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9 :
    print("You are severely Overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")