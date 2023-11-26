from random import randint

def pick_word():
    pick = randint(0, len(WORDS)-1)
    return WORDS[pick]
def hangman():
    return None

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
                print(f"That is correct! ✔️\n")
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
    again = input("Play again? (Y/N): ")

    if again == "n" or again == "N":
        print("Thanks for your time, i hope you enjoyed the hangman! 🖖🖖🖖")
        return False
    else:
        return True



WORDS = ["hacker", "bounty", "kamehameha", "budokai", "genkidama", "supernova", "starfield", "intervals", "planet", "satellite"]
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
input("Welcome to the hangman! Dont try to fool me or you will hug the string sooner! 😈\n"
      "Guess the word, are you ready? (Press enter to continue)")
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
        letter = input("Choose a letter: ")
        if len(letter)>1:
            print("\nSo you are using tricks... Okay, two lifes less for you buddy, keep trying 👎👎 .\n")
            lifes-=2
            print(HANGMAN_DRAWINGS[-lifes-1])
            print(f"Your current word is: {''.join(sketchy_word)}")
        else:
            if letter in letters_pool:
                print("\nDude, you already tried that one. 🤡 Less hp YIKES! 🤡")
                lifes -= 1
                print(HANGMAN_DRAWINGS[-lifes-1])
                print(f"Your current word is: {''.join(sketchy_word)}")
            else:
                win, lifes = evaluate(word, letter, sketchy_word, lifes)
                if lifes>0 and not win:
                    print(f"Your current word is: {''.join(sketchy_word)}")
                    guess = input("Guess the word: ")
                    if guess == word:
                        break
                if letter != "":
                    letters_pool.append(letter)
        
        

    if lifes>0:
        print(f"🎉🎉🎉 The word is '{word}' . Congratulations! You win! 🎉🎉🎉")
    else:
        print("☠️  You have failed. Rest in peace. ☠️")

    keep_playing = play_again()
   
    