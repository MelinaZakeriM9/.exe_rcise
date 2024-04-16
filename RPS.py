import random
import time

Define = {
    "rock": -1,
    "paper": 0,
    "scissors": 1
}

cDef ={
    -1: 'rock',
    0: 'paper',
    1: 'scissors'
}

plyrSC = 0
compSC = 0 

while (plyrSC and compSC) < 3:
    player = input("Please select Rock, Paper, or Scissors\n")
    player = player.lower()

    if player in Define:
        player = Define[player]
    


    rnd = random.Random(time.time())
    comp = rnd.randrange(-1,2)


    if player == comp:
        print("Computer chose", cDef[comp])
        print("Draw!\n")
    elif player == comp+1 or (player == -1 and comp == 1):
        print("Computer chose", cDef[comp])
        print("Win!!!\n")
        plyrSC += 1
    elif player == comp-1 or (player == 1 and comp == -1):
        print("Computer chose", cDef[comp])
        print("Lost...\n")
        compSC += 1
    else:
        print("That's not an option >:(\n")


if plyrSC == 3:
    print("player Wins!")
elif compSC == 3:
    print("Computer Wins...")


