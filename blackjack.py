import random
import sys
logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           '''
print(f"Welcome to BlackJack game \n{logo}\n Try your luck and play the game :)\n")
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player=[]
com=[]
for i in range(1,3):
    player.append(random.choice(card))
    com.append(random.choice(card))
print(f"Your deck is {player}:{sum(player)}\n")
print(f"The dealer deck is {com[0]} with an another card\n")

def dborrow():
        com.append(random.choice(card))
        if(sum(com)>sum(player) and sum(com)<22):
            print("You Loose, Better Luck Next time :) \n")
            display()
            sys.exit(0)
        elif(sum(player)==sum(com) and sum(com)>18):
            print("It's a draw, good play :) \n")
            display()
            sys.exit(0)
        elif(sum(player)==sum(com) and sum(com)<=18):
            dborrow()
        elif(sum(com)<sum(player)):
            dborrow()
        elif(sum(com)>21):
            print("Hurray You win!!\n")
            display()
            sys.exit(0)
        else:
            print("an error, please report this will help")


def display():
    print("The deck of both you and dealer were as below\n")
    print(f"The dealer had:{com}: {sum(com)}\n")
    print(f"You had:{player}:{sum(player)}\n")


def computerplay():
    if(sum(player)==sum(com) and sum(com)>18):
        print("It's a draw, good play :) \n")
        display()
        sys.exit(0)
    elif(sum(player)>sum(com) and sum(player)<=18):
        dborrow()
    elif(sum(player)<sum(com)):
        print("You Loose, Better Luck next time :)\n")
        display()
        sys.exit(0)
    elif(sum(player)>sum(com) and sum(player)>18):
        print("Hurray You Win!!\n")
        display()
        sys.exit(0)
    else:
        print("It's a error, can you please report this error to the coder\n it will help: ",com[0])


def player1():
    a=input("Please enter 'yes' if you want try a card else enter 'no' to stand your position: ")
    if(a=="yes"):
        player.append(random.choice(card))
        if(sum(player)>21):
            print("It's a bust! :(\nYou Loose, better luck next time :)\n")
            display()
        else:
            print(f"Your Deck is {player}:{sum(player)}\n ")
            player1()
    elif(a=="no"):
        computerplay()
    else:
        print("Please enter a valid option and try again\n")
        player1()


player1()

    



        
            

