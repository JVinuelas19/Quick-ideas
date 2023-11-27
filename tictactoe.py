from random import randint
import time
import os 

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

IA_QUOTES = ["Sick move Bobby",
             "I bet you can't beat my grandma", 
             "Is that all you got?", 
             "You should ask me for a lesson", 
             "Are you trolling?", 
             "[TRASH_TALK_QUOTE_69]",
             "Do you enjoy being so ridiculous?",
             "Is dumb your surname?",
             "LMAO do you imagine losing to a python random module?",
             "I call this the POGGERS! move",
             "Please call me i am entering madness writing this quotes -> www.github.com/JVinuelas19",
             "Have you ever heard about @Ornithob0t X account? Me neither.",
             "I'm tired boss",
             "Ha! That's what your mama said",
             "LEEEEEROY JEEEEENKINS",
             "HAHA another funny IA randomized quote",
             "Please help me",
             "German joke: Knock, knock. Who's there? DOESN'T MATTER OPEN THE DOOR NOW",
             "Another german joke: Why did the chicken crossed the road? HE WAS FOLLOWING ORDERS",
             "You will have more fun playing League of Legends",
             "Damn you never quit, right?",
             "You are like lambda functions: short!",
             "YIKES"  ]


def show_board(board):
    return(f" {board[0][0]} | {board[0][1]} | {board[0][2]} \n"
           f"---|---|---\n"
           f" {board[1][0]} | {board[1][1]} | {board[1][2]} \n"
           f"---|---|---\n"
           f" {board[2][0]} | {board[2][1]} | {board[2][2]} \n")


def reset_board(board):
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            board[i][j] = " "


def instructions():
     input("\nGrid positions are designed like the numpad:\n\n"
                  " 7 | 8 | 9 \n"
                  "---|---|---\n"
                  " 4 | 5 | 6 \n"
                  "---|---|---\n"
                  " 1 | 2 | 3 \n\n"
                  "Just enter the number to display your option.\n"
                  "Press enter to continue\n"
            )


def check_winner(multiplayer):
    #Columns
    if board[0][0] == board[1][0] == board[2][0] != " ":
        if board[0][0] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    if board[0][1] == board[1][1] == board[2][1] != " ":
        if board[0][1] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    if board[0][2] == board[1][2] == board[2][2] != " ":
        if board[0][2] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    #Rows
    if board[0][0] == board[0][1] == board[0][2] != " ":
        if board[0][0] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    if board[1][0] == board[1][1] == board[1][2] != " ":
        if board[1][0] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    if board[2][0] == board[2][1] == board[2][2] != " ":
        if board[2][0] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    #Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        if board[0][0] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        if board[0][2] == "X":
            if multiplayer:
                print("Player 1 wins!\n")
            else:
                print("You win!\n")
        else:
            if multiplayer:
                print("Player 2 wins!\n")
            else:
                print("You lose!\n")
        return True
    return False
    


def player_turn(option, value):
    if option == 7:
        board[0][0] = value
    elif option == 8:
        board[0][1] = value
    elif option == 9:
        board[0][2] = value
    elif option == 4:
        board[1][0] = value
    elif option == 5:
        board[1][1] = value
    elif option == 6:
        board[1][2] = value
    elif option == 1:
        board[2][0] = value
    elif option == 2:
        board[2][1] = value
    elif option == 3:
        board[2][2] = value
        

def play(multiplayer):
    positions = [1,2,3,4,5,6,7,8,9]
    over = False
    is_my_turn = True
    while(not over):
        try:
            if is_my_turn:
                if multiplayer:
                    option = int(input("Player 1 turn (1-9): "))
                else:
                    option = int(input("It's your turn (1-9): "))
                if option not in positions:
                    print("You must type a number from 1 to 9.")
                else:
                    player_turn(option, "X")
                    is_my_turn = False
                    positions.remove(option)
                    print(show_board(board))
                if len(positions) == 0:
                    over = True
                    if check_winner(multiplayer) is False:
                        print("It's a draw!\n")
                    break

            elif not is_my_turn:
                if multiplayer:
                    returned = int(input("Player 2 turn (1-9): "))
                    if returned not in positions:
                        print("You must type a number from 1 to 9.")
                    else:
                        player_turn(returned, "O")
                        is_my_turn = True
                        positions.remove(returned)
                        print(show_board(board))
                else:
                    print(IA_QUOTES[randint(0, len(IA_QUOTES)-1)])
                    time.sleep(2)
                    returned = positions.pop(randint(0, len(positions)-1))
                    player_turn(returned, "O")
                    is_my_turn = True
                    print(show_board(board))
            else:
                print("You must type a number from 1 to 9.")
        except:
            print("You must type a number from 1 to 9.")

        over = check_winner(multiplayer)
        



def main():
    os.system("cls")
    option = 0
    while (option!=4):
        try:
            option = int(input("Welcome to Tic Tac Toe game!\n"
                            "Select gamemode:\n"
                            "1 - Singleplayer\n"
                            "2 - Multiplayer \n"
                            "3 - How to play \n"
                            "4 - Exit        \n"))
            if option == 1:
                os.system("cls")
                play(multiplayer=False)
                reset_board(board)
            elif option == 2:
                os.system("cls")
                play(multiplayer=True)
                reset_board(board)
            elif option == 3:
                os.system("cls")
                instructions()
                os.system("cls")
            elif option == 4:
                os.system("cls")
                print("Thanks for playing Tic Tac Toe!\n"
                    "Check me out at www.github.com/JVinuelas19")
            else:
                os.system("cls")
                print("Option not available. Please try again.\n")

                
        except ValueError:
            os.system("cls")
            print("Option not available. Please try again.\n")


if __name__ == "__main__":
    main()