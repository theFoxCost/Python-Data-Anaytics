import random


povs = ('paper', 'rock', 'scissor')
# make a fction that gerate the BOT POV


rand = random.randrange(0,3)
botpov = str(povs(rand))

# make a fcntion to let the user enter it opinion
def userPOV():
    print("1. paper\n2. rock \n3. scissor")
    choice = int(input("Enter your Choice"))
    if choice == 1:
        userPOV = 'paper'
    elif choice == 2:
        userPOV = 'rock'
    elif choice == 3:
        userPOV = 'scissor'
    else:
        print("are you dumb")
    
    return userPOV

def compareBOTndUSER():
    if userPOV == botpov:
        print("DRAW")
    if userPOV != botpov:
        if userPOV == "paper" and botpov == "rock":
            print("HUMAN winns")
        elif userPOV == "rock" and botpov == "paper":
            print("BOT winns")
        elif userPOV == "paper" and botpov == "scissor":
            print("BOT winns")
        elif userPOV == "rock" and botpov == "paper":
            print("BOT winns")
        elif userPOV == "scissor" and botpov == "Rock":
            print("BOT winns")
        elif userPOV == "scissor" and botpov == "Rock":
            print("BOT winns")
        elif userPOV == "scissor" and botpov == "Rock":
            print("BOT winns")
         
        
        

# make a fcntion to let the user knwo the scor

