String = input("Enter a word")
Character = input("Enter the Character")
i = 0
Count=0
while(i<len(String)):
    if (String[i]==Character):
        Count = Count+1
    i=i+1
print("The number of times the Character has occured",Count)
            