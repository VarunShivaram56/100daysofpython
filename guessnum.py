import random
import sys
n=random.randint(1,100)
logo="""
                                                                                          
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___   ( ) _ \_   _  ___  ___ ___     _ __  _   _ _ __ ___  
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |/ /_\/ | | |/ _ \/ __/ __|   | '_ \| | | | '_ ` _ \ 
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | / /_\\| |_| |  __/\__ \__ \   | | | | |_| | | | | | |
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \____/ \__,_|\___||___/___/___|_| |_|\__,_|_| |_| |_|
                                                                              |_____|                     
"""
print(logo)#prints the logo
#asks for a choice
a=int(input("\nHello Participant, Great day \n So what difficulty level do you expect\n1.Easy\n2.Difficult\n"))#takes 1 or 2 as input for easy and difficult respectively
b=True
if(a==1):
    print("\nYou have 10 Chances to predict the number\n")
    c=10
elif(a==2):
    print("\nYou have 5 Chances to predict the number\n")
    c=5
else:
    print("\nI think you have chosen a wrong number, try again:)\n")
    sys.exit(0)
print("Best of Luck!! :)")
while(b and c!=0):
    print(f"\nNumber of Chances left are {c}")
    d=int(input("\nGuess the number: "))
    if(d<1 and d>100):
        print("Hint:Out of Range, Try to guess the number between 1 and 100")
        c-=1
    if(d>n):
        print("\nToo high")
        c-=1
    elif(d<n):
        print("\nToo low")
        c-=1
    elif(d==n):
        print("Hurray, You guessed it Right \n Congratulations :)")
        b=False
    else:
        print("\n An error")
print("\nIt was nice game..")