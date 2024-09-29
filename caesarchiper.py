
j=input("Press 'E' to encode and 'D' to decode:")
if(j=='E'):
    a=input("Enter the Text you want to encode(make sure there are no spaces):")
    b=int(input("Enter the no of shifts you need while encoding "))
    list1=[]
    for i in range(0,len(a)):
        if(a[i]==" "):
            list1.append('&')
            continue
        elif((ord(a[i])+b)>122):
            d=((ord(a[i])+b)%122)+97
        else:
            d=(ord(a[i])+b)
        list1.append(chr(d))
    c="".join(list1)
    print("The Encoded Script is ",c)
elif(j=='D'):
    a=input("Enter the Text you want to decode:")
    b=int(input("Enter the key:"))
    list1=[]
    for i in range(0,len(a)):
        if(a[i]=="&"):
            list1.append(' ')
            continue
        elif((ord(a[i])-b)<97):
            d=(ord(a[i])-b)+26
        else:
            d=(ord(a[i])-b)
        list1.append(chr(d))
    c="".join(list1)
    print(list1)
    print("The Decoded Script is ",c)
else:
    print("You have chosen a wrong option")

# list1=['a','b','c',' ','m']
# list1.append('m')
# list1.append(' ')
# list1.append('m')
# c="".join(list1)
# print("The Decoded Script is ",c)
# a=input()
# d=list(a)
# print(len(a),len(d))
# c="".join(d)
# print(len(c))