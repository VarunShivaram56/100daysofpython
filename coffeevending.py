milk=1000
water=2000
coffee=200
money=0
types=[
    {"name":"expresso",
     'm':0,'w':50,'c':18},
     {'name':"latte",'m':150,'w':200,'c':24},
     {'name':'cappuccino','m':100,'w':250,'c':24}
]
def count(penny,nickels,dimes,quarter,total):
    global money
    amt=0.01*penny+0.05*nickels+0.1*quarter+0.25*quarter
    if(amt<total):
        return 'less'
    elif(amt>=total):
        money=money+total
        return amt-total
    else:
        print('\nerror')
        exit()
def makecoffee(type):
    global water,coffee,milk
    if(type=='expresso'):
        t=types[0]
    elif(type=='latte'):
        t=types[1]
    elif(type=='cappuccino'):
        t=types[2]
    else:
        print("\nerror")
        exit()
    if(water>=t['w'] and milk>=t['m'] and coffee>=t['c']):
        pass
    else:
        return False
    milk=milk-t['m']
    water=water-t['w']
    coffee=coffee-t['c']
    return True   
def vending():
    global money
    cost=[1.5,2.5,3]
    print(f"\ncost of expresso is :{cost[0]}\ncost of latte is :{cost[1]}\ncost of cappuccino is:{cost[2]}\n")
    cof=input("\nWhich type of coffee do you need (expresso/latte/cappuccino):")
    p=int(input("\nPlease Enter the number of pennies:"))
    n=int(input("\nPlease enter the number of Nickels:"))
    d=int(input("\nPlease enter the number of dimes:"))
    q=int(input("\nPlease enter the number of quarters:"))
    if(cof=='expresso'):
        m=cost[0]
        r=count(p,n,d,q,m)
    elif(cof=='latte'):
        m=cost[1]
        r=count(p,n,d,q,m)
    elif(cof=='cappuccino'):
        m=cost[2]
        r=count(p,n,d,q,m)
    else:
        print('\nerror')
        exit()
    if(r=='less'):
        print("\nSorry you have given less money try again")
        vending()
    else:
        a=makecoffee(cof)
        if(a==False):
            print("\nSorry there is a shortage in resources")
            print("\nYour money is refunded")
            money=money-m
            vending()
        else:
            print("\nHere's your coffee")
            print(f"\nYou change is :{r} ")
            print("\nThankyou please come again... :)")
def report():
    global milk,money,water,coffee
    print(f"\nWater :{water}\nMilk :{water}\nCoffee:{coffee}\nMoney:{money}")
while(True):
    op=input("\nWelcome please enter your option vending or off or report ")
    if(op=='off'):
        exit()
    elif(op=='report'):
        report()
    elif(op=='vending'):
        vending()
    else:
        print("\nError")

            
