print("Enter marks obtained in 5 subjects")
Math=int(input("Enter the math marks"))
Science=int(input("Enter the science marks"))
Social=int(input("Enter the Social marks"))
Hindi=int(input("Enter the Hindi marks"))
English=int(input("Enter the Englsh marks"))
sum=Math+Science+Social+Hindi+English
average=sum/5
if average >= 91 and average<=100:
    print("Your grade is A1")
elif average>= 81 and average<=90:
    print("Your grade is A2")
elif average>= 71 and average<=80:
    print("Your grade is B1")
elif average>= 61 and average<=70:
    print("Your grade is B2")
elif average>= 51 and average<=60:
    print("Your grade is C1")
elif average>= 41 and average<=50:
    print("Your grade is C2")
elif average>= 31 and average<=40:
    print("Your grade is D1")
elif average>= 21 and average<=30:
    print("Your grade is D2")
elif average>= 11 and average<=20:
    print("Your grade is E1")
elif average>= 1 and average<=10:
    print("Your grade is E2")
else:
    print("Invalid")
