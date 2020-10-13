#Simple game of Hangman that runs in the terminal
from os import system, name
import random
wordlist = [
    ["pizza","food"],
    ["hamburger","food"],
    ["africa","continent"],
    ["canada","country"],
    ["sandwich","food"],
    ["assbutt","obscenity"],
    ["cheese","food"],
    ["apple","food"],
    ["birth","medical"],
    ["disease","medical"],
    ["horror","feeling"],
    ["power","feeling"],
    ["hardcore","feeling"],
    ["hilarity","feeling"],
    ["myopia","medical"],
    ["cat","animal"],
    ["dog","animal"],
    ["alligator","animal"],
    ["caterpillar","animal"],
    ["chair","furniture"],
    ["bed","furniture"],
    ["computer","electronics"],
    ["europe","continent"],
    ["asia","continent"],
    ["skull","medical"],
    ["marsh","environment"],
    ["desert","environment"],
    ["swamp","environment"],
    ["lagoon","environment"],
    ["shit","obscenity"],
    ["fuck","obscenity"],
    ["potato","food"],
    ["ethereal","thing"],
    ["corporate","thing"],
    ["high","feeling"],
    ["low","feeling"],
    ["speedy","feeling"],
    ["tetherball","sport"],
    ["football","sport"],
    ["hockey","sport"],
    ["swimming","sport"],
    ["basketball","sport"],
    ["tennis","sport"],
    ["0","number"],
    ["1","number"],
    ["2","number"],
    ["3","number"],
    ["4","number"],
    ["5","number"],
    ["6","number"],
    ["7","number"],
    ["8","number"],
    ["9","number"]
]
wordbag = []
def Main():
    #Terminal drawing
    def DrawGame():
        #Clear contents of Windows/Mac/Linux Terminal
        if name == "nt":
            system("cls")
        else:
            system("clear")
        #Start
        print("\n")
        #Title
        print("Welcome to Hangman")
        #Graphic
        print("_________")
        print("|     |")
        print("|     |")
        print("|     "+("O" if failCount > 0 else ""))
        print("|    "+
        ("/" if failCount > 1 else "")+
        ("|" if failCount > 2 else "")+
        ("\\" if failCount > 3 else ""))
        print("|     "+("|" if failCount > 4 else ""))
        print("|    "+
        ("/ " if failCount > 5 else "")+
        ("\\" if failCount > 6 else ""))
        print("|     ")
        print("IIIIIIIII")
        #Word Lettering
        print(f"\nThe word is:   {''.join(hiddenWord)}  (Hint: {hint})")
        #Status Messages
        print(f"\nYou have {maxFails-failCount} attempt(s) left...")
        print(f"\n       {message}")
        print(f"\n       {gameOverMessage}\n")
        #End
    def RandomWord():
        global wordbag
        #Return a randomly chosen word from the bag and remove it from availability
        if not wordbag:
            wordbag = list(wordlist)
        chosen = wordbag.pop(random.choice(range(len(wordbag))))
        return chosen
    #Game setup
    hiddenWord = []
    guessedLetters = []
    failCount = 0
    maxFails = 7
    message = ""
    gameOverMessage = ""
    game_over = False
    choice = RandomWord()
    word = choice[0].upper()
    hint = choice[1].lower().capitalize()
    for _null in word:
        hiddenWord.append("_ ")
    #Start game
    while not game_over:
        #Render the game graphics
        DrawGame()
        #Check input from player and see if it's a letter in the word
        userInput = input("Press a letter and then enter to spell out the word: ")
        userInput = userInput.upper()
        #Invalid guess
        if len(userInput) > 1 or len(userInput) == 0 or userInput == " ":
            message = f"Invalid input: '{userInput}'. Must be a single character."
        #Duplicate guess
        elif userInput in guessedLetters:
            message = f"You already guessed '{userInput}'."
        #Correct guess
        elif userInput in word:
            message = f"Good. '{userInput}' is a letter in the word."
            for i in range(len(word)):
                #Replace hidden letter with word letter plus spacing
                letter = word[i]
                if letter == userInput:
                    hiddenWord[i] = word[i] + " "
            guessedLetters.append(userInput)
        #Incorrect guess
        else:
            guessedLetters.append(userInput)
            failCount+=1
            message = f"Nope. '{userInput}' is not a letter in the word."
        #Win
        if all("_ " != char for char in hiddenWord):
            game_over = True
            message = "Congratulations. You've saved a convict from justice."
            gameOverMessage = "Game Over. You Win."
        #Lose
        if failCount >= maxFails:
            #Reveal word
            for i in range(len(word)):
                hiddenWord[i] = word[i] + " "
            game_over = True
            message = "Sorry, your man's been hanged."
            gameOverMessage = "Game Over. You Lose."
    #Game over, see if user wants to play again
    while True:
        #Render loop again
        DrawGame()
        userInput = input("Play again? (Y/N): ")
        #Depending on input, either reset game, exit or wait for proper input
        userInput = userInput.lower()
        if userInput == "y":
            Main()
            break
        elif userInput == "n":
            break
        else:
            continue
#Initialize
Main()