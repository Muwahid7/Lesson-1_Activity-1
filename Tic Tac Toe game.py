import random
def create_board():
    return [["" for _ in range(3)]for _ in range(3)]
def print_board(board):
    print("\n current board")
    for row in board:
        print("|".join(row))
        print("-"*5)
def check_winner(board,player):
    for row in board:
        if all(cell==player for cell in row):
            return True
    for col in range(3):
        if all (board[row][col]==player for row in range(3)):
            return True
    if all (board[i][i]==player for i in range(3)):
        return True
def is_draw(board):
        return all(cell!=""for row in board for cell in row)
def get_move(player):
    while True:
        try:
            row = int(input(f"player {player},enter row(0-2)"))
            col = int(input(f"player {player},enter col(0-2)"))
            if row in range(3)and col in range(3):
                return row,col
            else:
                print("Invalid input")
        except ValueError:
            print("Enter a valid number")
def play_game():
    board=create_board()
    current_player = random.choice(["x","o"])
    print(f"{current_player}starts")
    while True: 
        print_board(board)
        row,col = get_move(current_player)
        if board[row][col]!="":
            print("cell already taken,try again")
            continue
        board[row][col]=current_player
        if check_winner(board,current_player):
            print_board(board)
            print(f"{current_player}player wins")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw")
            break
        current_player = "o" if current_player == "x" else "x"
if __name__ =="__main__":
    play_game()
