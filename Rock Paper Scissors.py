import random
while True:
    user_action = input("Enter a choice(Rock/Paper/Scissor)")
    Possible_actions = ["Rock","Paper","Scissor"]
    Computer_Action = random.choice(Possible_actions)
    print(f"\n You choose{user_action},Computer choose{Computer_Action}")
    if user_action == Computer_Action:
        print("both players selected {user_action}.It's a tie")
    elif user_action == "Rock":
        if Computer_Action == "Scissors":
            print("Rock smashes scissor!!!,You win")
        else:
            print("Paper covers rock,You Lose")
    elif user_action == "Paper":
        if Computer_Action == "Rock":
            print("Paper covers rock!!!,You win")
        else:
            print("Scissors cut paper,You Lose")
    elif user_action == "Scissors":
        if Computer_Action == "Paper":
            print("Scissor cuts paper!!!,You win")
        else:
            print("Rock smashes scissor,You Lose")
    play_again=input("Play again(y/n)")
    if play_again!="y":
        break