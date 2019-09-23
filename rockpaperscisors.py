#Rock paper sicsors game

import random
while True:
    userresponse = input("hello there and welcome to rock paper scisors game, if you would like to play, press y, or quit program, to leave")
    if userresponse == "quit program":
        break
    elif userresponse == "y":
        print("Welcome to rock paper scisors")
        

    x = ["rock", "paper", "scisors"]
    random.choice(x)
    for var in x:
        decision = input("Choose, rock, paper or scisors\n")
        if var == "rock" and decision =="scisors":
            print("The computer has ", var)
            print("You have ", decision)
            print("COMPUTER wins")
        elif var == "scisors" and decision == "scisors":
            print("The computer has ", var)
            print("You have ", decision)
            print("TIE GAME")
        elif var == "paper" and decision ==  "scisors":
            print("The computer has ", var)
            print("You have ", decision)
            print("YOU WIN")
        elif var == "rock" and decision == "paper":
            print("The computer has ", var)
            print("YOU got ", decision)
            print("YOU WIN")
        elif var == "scisors" and decision =="paper":
            print("The computer has ", var)
            print("You have ", decision)
            print("COMPUTER wins")
        elif var == "paper" and decision == "paper":
            print("The computer has ", var)
            print("You have ", decision)
            print("TIE GAME")
        elif var == "rock" and decision ==  "rock":
            print("The computer has ", var)
            print("You have ", decision)
            print("TIE GAME")
        elif var == "scisors" and decision == "rock":
            print("The computer has ", var)
            print("YOU got ", decision)
            print("YOU WIN")
        elif var == "paper" and decision == "rock":
            print("The computer has ", var)
            print("YOU got ", decision)
            print("YOU lose")


     
        
        


