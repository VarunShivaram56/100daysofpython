import data
main='''
      ___                       ___           ___                    ___           ___              
     /\__\          ___        /\  \         /\__\                  /\  \         /\  \             
    /:/  /         /\  \      /::\  \       /:/  /                 /::\  \       /::\  \            
   /:/__/          \:\  \    /:/\:\  \     /:/__/                 /:/\:\  \     /:/\:\  \           
  /::\  \ ___      /::\__\  /:/  \:\  \   /::\  \ ___            /:/  \:\  \   /::\~\:\  \          
 /:/\:\  /\__\  __/:/\/__/ /:/__/_\:\__\ /:/\:\  /\__\          /:/__/ \:\__\ /:/\:\ \:\__\         
 \/__\:\/:/  / /\/:/  /    \:\  /\ \/__/ \/__\:\/:/  /          \:\  \ /:/  / \/_|::\/:/  /         
      \::/  /  \::/__/      \:\ \:\__\        \::/  /            \:\  /:/  /     |:|::/  /          
      /:/  /    \:\__\       \:\/:/  /        /:/  /              \:\/:/  /      |:|\/__/           
     /:/  /      \/__/        \::/  /        /:/  /                \::/  /       |:|  |             
     \/__/                     \/__/         \/__/                  \/__/         \|__|             
      ___       ___           ___                                                                   
     /\__\     /\  \         /\__\                                                                  
    /:/  /    /::\  \       /:/ _/_                                                                 
   /:/  /    /:/\:\  \     /:/ /\__\                                                                
  /:/  /    /:/  \:\  \   /:/ /:/ _/_                                                               
 /:/__/    /:/__/ \:\__\ /:/_/:/ /\__\                                                              
 \:\  \    \:\  \ /:/  / \:\/:/ /:/  /                                                              
  \:\  \    \:\  /:/  /   \::/_/:/  /                                                               
   \:\  \    \:\/:/  /     \:\/:/  /                                                                
    \:\__\    \::/  /       \::/  /                                                                 
     \/__/     \/__/         \/__/                                                                  
'''
vs='''
 _          _       _        
/\ \    _ / /\     / /\      
\ \ \  /_/ / /    / /  \     
 \ \ \ \___\/    / / /\ \__  
 / / /  \ \ \   / / /\ \___\ 
 \ \ \   \_\ \  \ \ \ \/___/ 
  \ \ \  / / /   \ \ \       
   \ \ \/ / /_    \ \ \      
    \ \ \/ //_/\__/ / /      
     \ \  / \ \/___/ /       
      \_\/   \_____\/        
                             
'''
def compare(x,y):
    if(x["followers"]>y["followers"]):
        return True
    else:
        return False 

print(data,'\n')
print("Welcome to \"HIGH OR LOW\" Game\n")
print("The rule is simple choose the one who has more instagram followers... :)\n\n")
score=0
b=True
p=data.choose()
while(b):
    q=data.choose()
    print(f"\nA. {p["name"]} from the country {p["country"]}\n")
    print(vs)
    print(f"\nB. {q["name"]} from the country {p["country"]}\n")
    a=input("Please enter your option: ")
    if(a=='A'):
        b=compare(p,q)
        print(f"\n{p["name"]} had {p["followers"]} and {q["name"]} had {q["followers"]}\n")
        if(b==True):
            score+=1
            continue
    else:
        b=compare(q,p)
        print(f"\n{p["name"]} had {p["followers"]} and {q["name"]} had {q["followers"]}\n")
        if(b==True):
            p=q
            score+=1
            continue
print("You Loose :( \n")
print(f"\nYour Final Score is :{score}")