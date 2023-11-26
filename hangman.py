from random import randint
import os


def pick_word():
    with open("words.txt", "r") as words:
        word_list = words.readlines()
        pick = word_list[randint(0, WORDS)].replace("\n", "").lower()
    return pick


def sketch(word):
    sketchy_list = list()
    for letter in word:
        if letter != "-":
            sketchy_list.append("_")
        else:
            sketchy_list.append("-")
    return sketchy_list


def update_sketchy(word, letter, sketchy_word):
    for i, current_letter in enumerate(sketchy_word):
        if letter == word[i]:
            sketchy_word[i] = letter
    return sketchy_word


def evaluate(word, letter, sketchy_word, lifes):
    win = False
    if letter in word and letter != "":
            sketchy_word = update_sketchy(word, letter, sketchy_word)
            if "_" in sketchy_word:
                print(f"That is correct! ✔️")
                print(HANGMAN_DRAWINGS[-lifes-1])
            else:
                win = True
    else:
        if (letter != ""):
            print(f"Letter {letter} is not found! ❌")
        else:
            print("Empty letters will not save you from the gallows. Take this hit: 🥊 ")
        lifes-=1
        print(HANGMAN_DRAWINGS[-lifes-1])
    
    return win, lifes


def play_again():
    again = input("Play again? (Type 'n' or 'N' to end)): ")

    if again == "n" or again == "N":
        print("Thanks for your time, i hope you enjoyed the hangman! 🖖🖖🖖")
        return False
    else:
        return True


WORDS = 1000
LIFES = 6
HANGMAN_DRAWINGS = [" ___    \n"
                    "|   |   \n"
                    "|       \n"
                    "|       \n"
                    "|       \n"
                    "|_______\n", 
                    " ___    \n"
                    "|   |   \n"
                    "|   O   \n"
                    "|       \n"
                    "|       \n"
                    "|_______\n", 
                    " ___    \n"
                    "|   |   \n"
                    "|   O   \n"
                    "|   |   \n"
                    "|       \n"
                    "|_______\n", 
                    " ___    \n"
                    "|   |   \n"
                    "|   O   \n"
                    "|  /|   \n"
                    "|       \n"
                    "|_______\n", 
                    " ___    \n"
                    "|   |   \n"
                    "|   O   \n"
                    "|  /|\  \n"
                    "|       \n"
                    "|_______\n", 
                    " ___    \n"
                    "|   |   \n"
                    "|   O   \n"
                    "|  /|\  \n"
                    "|  /    \n"
                    "|_______\n",
                    " ___    \n"
                    "|   |   \n"
                    "|   O    JUST GUESS IT GOD DAMMIT\n"
                    "|  /|\  \n"
                    "|  / \    BTW WHERE'S MY OXYGEN?\n"
                    "|_______\n", 
                    ]

def main():
    input("Welcome to the hangman! Dont try to fool me or you will hug the string sooner! 😈\n"
        "Guess the word, are you ready? (Press enter to continue)")
    os.system("cls")
    keep_playing = True
    while(keep_playing):
        letters_pool = list()
        word = pick_word()
        sketchy_word = list(sketch(word))
        lifes = LIFES
        win = False
        while(lifes>0 and not win):
            used_letters = [x for x in letters_pool if (len(x)==1 and x not in used_letters)]
            if len(used_letters)>0:
                print(f"Used letters: {','.join(letters_pool)}\n")
            letter = input("Choose a letter: ").lower()
            print(letter)
            os.system("cls")

            if len(letter)>1:
                print("So you are using tricks... Okay, two lifes less for you buddy, keep trying 👎👎")
                lifes-=2
                if lifes<0:
                    lifes = 0
                print(HANGMAN_DRAWINGS[-lifes-1])
                print(f"Your current word is: {''.join(sketchy_word)}")
            else:
                if letter in letters_pool:
                    print("Dude, you already tried that one. 🤡 Less hp YIKES! 🤡")
                    lifes -= 1
                    print(HANGMAN_DRAWINGS[-lifes-1])
                    print(f"Your current word is: {''.join(sketchy_word)}")
                else:
                    win, lifes = evaluate(word, letter, sketchy_word, lifes)
                    if lifes>0 and not win:
                        print(f"Your current word is: {''.join(sketchy_word)}")
                        if letter != "":
                            guess = input("Guess the word: ").lower()
                            if guess == word:
                                break
                            letters_pool.append(letter)
            
            
        print(f"The word is '{word}'") 
        if lifes>0:
            print(f"🎉🎉🎉 Congratulations! You win! 🎉🎉🎉")
        else:
            print("☠️  You have failed. Rest in peace. ☠️")

        keep_playing = play_again()
        if keep_playing:
            os.system("cls")
   

if __name__ == "__main__":
    main()