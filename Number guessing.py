import random
def number_guessing_game():
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100")
    while True:
        try:
            guess = int(input("Enter your guess"))
            attempts+=1
            if guess<number_to_guess:
                print("too low,try again")
            elif guess>number_to_guess:
                print("too high,try again")
            else:
                print(f"correct,the number was{number_to_guess}")
                print(f"you guessed it in{attempts}attempts")
                break
        except ValueError:
            print("Please enter a valid number")
number_guessing_game()