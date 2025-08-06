class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__ (self):
        return self.word +'('+self.meaning+')'
flash = []
print("Welcome to flashcard application")
while (True):
    word = input("Enter the name u want to add to flashcard")
    meaning = input("Enter the meaning of the word")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter zero if u want to add another flashcard else Enter 1"))
    if(option):
        break
print("\n your flashcards")
for i in flash:
    print(">",i)