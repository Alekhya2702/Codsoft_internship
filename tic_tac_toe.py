board = [" " for x in range(9)]
def display_board():
    r1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    r2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    r3 = "| {} | {} | {} |".format(board[6], board[7], board[8])


    print()
    print(r1)
    print(r2)
    print(r3)
    print()

def player_move(c):
    if c == "X":
        number = 1
    elif c == "O":
        number = 2
    print("player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = c
    else:
        print()
        print("space is not empty,choose another space")
def is_victory(c):
    if (board[0] == c and board[1] == c and board[2] == c) or \
       (board[3] == c and board[4] == c and board[5] == c) or \
       (board[6] == c and board[7] == c and board[8] == c) or \
       (board[0] == c and board[3] == c and board[6] == c) or \
       (board[1] == c and board[4] == c and board[7] == c) or \
       (board[2] == c and board[5] == c and board[8] == c) or \
       (board[0] == c and board[4] == c and board[8] == c) or \
       (board[2] == c and board[4] == c and board[6] == c):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    display_board()
    player_move("X")
    display_board()
    if is_victory("X"):
        print("X wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        display_board()
        print("O wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break


