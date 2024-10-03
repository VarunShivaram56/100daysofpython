logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Hello Bidders! Excited to see you here get ready for the auction")
a=True
bid={}
while(a==True):
    
    b=input("Please enter 'yes' if you want to bid else 'no':\n")
    print("\n"*100)
    if(b=='yes'):
        print("\n\n")
        e=input("please enter your name:\n")
        if(e in bid):
            print("The person has already submitted their bid")
            continue
        c=int(input("Please enter your bidding amount:\n$"))
        bid.update({e:c})
    elif(b=='no'):
        a=False
    else:
        print("Please enter a valid option")
max = list(bid.keys())[0]
for key in bid:
    if(bid[key]>bid[max]):
        max=key
print("The Highest bidder among the participants is \n")
print(f"{max} with a bidding amount of {bid[max]}$\n")
print(f"Congratulations {max}!!!")