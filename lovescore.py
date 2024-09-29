def calculate_love_score(name1,name2):
    count1=count2=0;
    list1=['L','O','V','E']
    list2=['T','R','U','E']
    for i in name1.upper():
        if(i in list1):
            count1+=1
    for j in name2.upper():
        if(j in list1):
            count1+=1
    for i in name1.upper():
        if(i in list2):
            count2+=1
    for j in name2.upper():
        if(j in list2):
            count2+=1
    print(f"Love Score={count2}{count1}")  

calculate_love_score("Kanye West","Kim Kardashian")