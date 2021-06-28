contacts=dict()
contacts['ravi']=9090909090
while(True):
    print("Enter your option : ")
    print("1\tINSERT\n2\tDISPLAY\n3\tUPDATE\n4\tDELETE\n0\tCLOSE Contacts Book")
    opt=int(input())
    if(opt==1):
        name=input("Enter the name to add to Contacts Book:")
        if name in contacts:
            print(name,"already exists")
        else:
            contacts[name]=input("Enter the mobile number:")
    elif(opt==2):
        for i in contacts.keys():
            print(i,"   ",contacts[i])
    elif(opt==3):
        name=input("Enter name to update:")
        if name in contacts:
            contacts[name]=input("Enter the mobile number")
        else:
            print(name,"doesn't exists in Contacts")
    elif(opt==4):
        name=input("Enter name to delete:")
        if name in contacts:
            contacts.pop(name)
        else:
            print(name,"doesn't exists in Contacts")
    elif(opt==0):
        break
