email = input("Enter your email: ")
L,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if('@' in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        L=1
                    elif i.isalpha():
                        if i == i.upper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i == "-" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if L==1 or k==1 or d==1:
                    print("Invalid Email")
                else:
                    print("Valid Email")
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")            