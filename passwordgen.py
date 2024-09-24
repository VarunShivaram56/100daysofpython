import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
count=0
count1=0
while(len(password)<nr_letters):
    i=random.randint(1,3)
    if((count<nr_numbers)or(count1<nr_symbols)):
        if(i==1):
            password.append(random.choice(letters))
        elif(i==2):
            password.append(random.choice(numbers))
            count+=1
        else:
            password.append(random.choice(symbols))
            count1+=1
    else:
        break;
fnl=''.join(password)
print(fnl)
        
    