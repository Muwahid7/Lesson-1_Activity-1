import random
playing = True
number = str(random.randint(1,10))
print("Generate a number between 1 to 9")
print("The game ends when the user gets 1")
while playing:
    guess=input("Give me a good guess")
    if number == guess:
        print("you win the game")
        print("The number was",number)
        break
    else:
        print("Your guess was not right")
