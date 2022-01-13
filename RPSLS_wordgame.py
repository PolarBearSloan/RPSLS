#Tutorial followed TechWithTim Youtube 7Jan2022, The Big Bang Theory spin added
import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]
options[0]

while True:
    userInput = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to Quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0,4)
    #rock: 0, paper:1, scissors: 2, lizzard: 3, spock: 4
    computerPick = options[randomNumber]
    print("Computer picked", computerPick + ".")

    if userInput == "scissors" and computerPick == "paper":
        print("Scissors cut Paper. You won!!!")
        userWins += 1

    elif userInput == "paper" and computerPick == "rock":
        print("Paper covers Rock. You won!!!")
        userWins += 1

    elif userInput == "rocks" and computerPick == "lizard":
        print("Rock crushes Lizard. You won!!!")
        userWins += 1

    elif userInput == "lizard" and computerPick == "spock":
        print("Lizard poisons Spock. You won!!!")
        userWins += 1

    elif userInput == "spock" and computerPick == "scissors":
        print("Spock smashes Scissors. You won!!!")
        userWins += 1

    elif userInput == "scissors" and computerPick == "lizard":
        print("Scissors decapitate Lizard. You won!!!")
        userWins += 1

    elif userInput == "lizard" and computerPick == "paper":
        print("Lizard eats Paper. You won!!!")
        userWins += 1

    elif userInput == "paper" and computerPick == "spock":
        print("Paper disproves Spock. You won!!!")
        userWins += 1

    elif userInput == "spock" and computerPick == "rock":
        print("Spock vaporizes rock. You won!!!")
        userWins += 1

    elif userInput == "rock" and computerPick == "scissors":
        print("Rock smashes Scissors. You won!!!")
        userWins += 1
    else:
        print("You lost.")
        computerWins += 1

print("You won", userWins, "times.")
print("The Computer won", computerWins, "times.")
print("Goodbye!")