logo=""" 
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|"""
def calc(a):
    b=input("Please choose one of the following operators \n+\n-\n*\n/\nyour choice:")
    c=int(input("Please enter the second number:"))
    if(b=='+'):
        e=a+c
        print(f"{a}+{c}={e}\n")
    elif(b=='-'):
        e=a-c
        print(f"{a}-{c}={e}\n")
    elif(b=='*'):
        e=a*c
        print(f"{a}X{c}={e}\n")
    elif(b=='/'):
        e=a/c
        print(f"{a}/{c}={e}\n")
    f=input("If you want to continue calculation with the existing answer enter 'y' else enter 'n' for fresh calculation\n")
    if(f=='y'):
        calc(e)
    else:
        i="Thankyou for using me for calculations"
        return i
print(logo,"\n")
print("WELCOME to Varun's Calculator!!\n")
a=int(input("Please enter the first number: "))
h=calc(a)
print(h)
