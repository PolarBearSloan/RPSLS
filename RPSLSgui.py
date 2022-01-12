#Tutorial followed ADV.LEARNING YouTube 11Jan2022
from tkinter import *
from PIL import Image,ImageTk
import random

#Main Window
root = Tk()
root.geometry("1280x720")
root.title("Rok/Paper/Scissors/Lizard/Spock by Aaron Sloan")
root.configure(background = "black")

#Picture with resize
rock_img = Image.open("rock.png")
resize_rock = rock_img.resize((200,200), Image.ANTIALIAS)
newRock = ImageTk.PhotoImage(resize_rock)

paper_img = Image.open("paper.png")
resize_paper = paper_img.resize((200,200), Image.ANTIALIAS)
newPaper = ImageTk.PhotoImage(resize_paper)

scissors_img = Image.open("scissors.png")
resize_scissors = scissors_img.resize((200,200), Image.ANTIALIAS)
newScissors = ImageTk.PhotoImage(resize_scissors)

lizard_img = Image.open("lizard.png")
resize_lizard = lizard_img.resize((200,200), Image.ANTIALIAS)
newLizard = ImageTk.PhotoImage(resize_lizard)

spock_img = Image.open("spock.png")
resize_spock = spock_img.resize((200,200), Image.ANTIALIAS)
newSpock = ImageTk.PhotoImage(resize_spock)

logo_img = Image.open("RPSLS_logo.png")
resize_logo = logo_img.resize((500,500), Image.ANTIALIAS)
newLogo = ImageTk.PhotoImage(resize_logo)

#Insert Picture
player_label = Label(root,image=newRock,bg="black")
rules_label = Label(root,image=newLogo,bg="black")
comp_label = Label(root,image=newSpock,bg="black")
player_label.grid(row=6,column=1)
rules_label.grid(row=6,column=2)
comp_label.grid(row=6,column=3)

#Scores
playerScore = Label(root,text="0",font=300,bg="black",fg="white")
compScore = Label(root,text="0",font=300,bg="black",fg="red")
playerScore.grid(row=0,column=1)
compScore.grid(row=0,column=4)

#Indicators
playerInd = Label(root, font=50,text="PLAYER",bg="black",fg="white").grid(row=0,column=0)
compInd = Label(root, font=50,text="COMPUTER",bg="black",fg="red").grid(row=0,column=3)

#Messages
msg = Label(root,font=300,bg="teal",fg="black")
msg.grid(row=1,column=2)
def updateMsg(x):
    msg['text']=x
    
#Update Scores
def updatePlayerScore():
    playerWins = int(playerScore['text'])
    playerWins += 1
    playerScore['text']=str(playerWins)
def updateCompScore():
    compWins = int(compScore['text'])
    compWins += 1
    compScore['text']=str(compWins)
#Win Conditions
def checkWin(player,computer):
    if player == computer:
        updateMsg("It's a Tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMsg("Paper covers Rock. You Lost.")
            updateCompScore()
        elif computer == "spock":
            updateMsg("Spock vaporizes Rock. You Lost.")
            updateCompScore()
        elif computer == "lizard":
            updateMsg("Rock crushes Lizard. You Won!!!")
            updatePlayerScore()
        else:
            updateMsg("Rock crushes Scissors. You Won!!!")
            updatePlayerScore()
    elif player == "paper":
        if computer == "scissors":
            updateMsg("Scissors cuts Paper. You Lost.")
            updateCompScore()
        elif computer == "lizard":
            updateMsg("Lizard eats Paper. You Lost.")
            updateCompScore()
        elif computer == "rock":
            updateMsg("Paper covers Rock. You Won!!!")
            updatePlayerScore()
        else:
            updateMsg("Paper disproves Spock. You Won!!!")
            updatePlayerScore()    
    elif player == "scissors":
        if computer == "rock":
            updateMsg("Rock crushes Scissors. You Lost.")
            updateCompScore()
        elif computer == "spock":
            updateMsg("Spock smashes Scissors. You Lost.")
            updateCompScore()
        elif computer == "paper":
            updateMsg("Scissors cuts Paper. You Won!!!")
            updatePlayerScore()
        else:
            updateMsg("Scissors decapitates Lizard. You Won!!!")
            updatePlayerScore()
    elif player == "lizard":
        if computer == "rock":
            updateMsg("Rock crushes Lizard. You Lost.")
            updateCompScore()
        elif computer == "scissors":
            updateMsg("Scissors decapitates Lizard. You Lost.")
            updateCompScore()
        elif computer == "paper":
            updateMsg("Lizard eats Paper. You Won!!!")
            updatePlayerScore()
        else:
            updateMsg("Lizard poisons Spock. You Won!!!")
            updatePlayerScore()
    elif player == "spock":
        if computer == "paper":
            updateMsg("Paper disproves Spock. You Lost.")
            updateCompScore()
        elif computer == "lizard":
            updateMsg("Lizard poisons Spock. You Lost.")
            updateCompScore()
        elif computer == "rock":
            updateMsg("Spock vaporizes Rock. You Won!!!")
            updatePlayerScore()
        else:
            updateMsg("Spock smashes Scissors. You Won!!!")
            updatePlayerScore()
    else:
        pass
#Update Player and Computer label on pick
options = ["rock", "paper", "scissors", "lizard", "spock"]
#rock: 0, paper:1, scissors: 2, lizzard: 3, spock: 4
options[0]
def playerPick(x):
    if x=="rock":
        player_label.configure(image=newRock)
    elif x=="paper":
        player_label.configure(image=newPaper)
    elif x=="scissors":
        player_label.configure(image=newScissors)
    elif x=="lizard":
        player_label.configure(image=newLizard)
    else:
        player_label.configure(image=newSpock)
    compPick = options[random.randint(0,4)]
    if compPick=="rock":
        comp_label.configure(image=newRock)
    elif compPick=="paper":
        comp_label.configure(image=newPaper)
    elif compPick=="scissors":
        comp_label.configure(image=newScissors)
    elif compPick=="lizard":
        comp_label.configure(image=newLizard)
    else:
        comp_label.configure(image=newSpock)
    checkWin(x,compPick)
#Buttons
rock_button = Button(root,width=20,height=2,text="ROCK",bg="teal",fg="black",command=lambda:playerPick("rock")).grid(row=1,column=0)
paper_button = Button(root,width=20,height=2,text="PAPER",bg="teal",fg="black",command=lambda:playerPick("paper")).grid(row=2,column=0)
scissors_button = Button(root,width=20,height=2,text="SCISSORS",bg="teal",fg="black",command=lambda:playerPick("scissors")).grid(row=3,column=0)
lizard_button = Button(root,width=20,height=2,text="LIZARD",bg="teal",fg="black",command=lambda:playerPick("lizard")).grid(row=4,column=0)
spock_button = Button(root,width=20,height=2,text="SPOCK",bg="teal",fg="black",command=lambda:playerPick("spock")).grid(row=5,column=0)

root.mainloop()