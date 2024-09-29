
i=input("Press 'E' to encode and 'D' to decode:")
if(i=='E'):
    a=input("Enter the Text you want to encode(make sure there are no spaces):")
    b=int(input("Enter the no of shifts you need while encoding "))
    list1=[]
    for i in range(0,len(a)):
        if((ord(a[i])+b)>122):
            d=((ord(a[i])+b)%122)+97
        else:
            d=(ord(a[i])+b)
        list1.append(chr(d))
    c="".join(list1)
    print("The Encoded Script is ",c)
elif(i=='D'):
    a=input("Enter the Text you want to decode:")
    b=int(input("Enter the key:"))
    list1=[]
    for i in range(0,len(a)):
        if((ord(a[i])-b)<97):
            d=(ord(a[i])-b)+26
        else:
            d=(ord(a[i])-b)
        list1.append(chr(d))
    c="".join(list1)
    print("The Decoded Script is ",c)
else:
    print("You have chosen a wrong option")

