amount=int(input("Please enter the amount"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print(note_1)
print(note_2)
print(note_3)

