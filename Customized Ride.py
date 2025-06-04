print("Select the ride u need")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice"))
if (choice==1):
    print("What type of bike do u need")
    print("1.Royal Enfield")
    print("2.BMW Bike")
    choice2 = int(input("Enter your choice2"))
    if choice2==1:
        print("Royal Enfield is the bike u have choosen")
    else:
        print("You have chosen BMW bike")
elif (choice==2):
    print("What type of car  do u need")
    print("1.SUV")
    print("2.Sedan")
    choice3 = int(input("Enter your choice3"))
    if choice3==1:
        print("U have selected SUV")
    else:
        print("U have selcted Sedan")
else:
    print("Invalid input")
