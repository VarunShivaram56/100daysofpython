import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

list1=[rock,paper,scissor]
computer=random.choice(list1)
a=input("Please enter your choice between \"rock\",\"paper\",\"scissor\"\n(and make sure there is no typo)\n")
list2={"rock":rock,"paper":paper,"scissor":scissor}
print("You Chose:\n",list2[a])
print("The Computer Chose\n ",computer)
list3={rock:"rock",paper:"paper",scissor:"scissor"}
computer=list3[computer]


if(a.strip()==computer.strip()):
    print("It's a draw\nWanna Try Another Time!")
elif((a=="rock" and computer=="paper")or(a=="paper" and computer=="scissor")or(a=="scissor"and computer=="rock")):
    print("You Loose\nBetter Luck Next Time!")
else:
    print("You Win\nCongraulations")