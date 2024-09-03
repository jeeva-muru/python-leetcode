
def checkPrefix(passwords):
    
    for i in range(len(passwords)):
        for j in range(i,len(passwords)):
            prefix=passwords[i]
            # print(prefix)
            # print(password[j+1])
            length = len(prefix)
            
            # print("sliced string:", slicing)
            if((j+1)<len(passwords)):
                slicing = passwords[j+1][:len(prefix)]
                # print("prefix:",prefix)
                # print("slicing:", slicing)
                if(prefix == slicing):
                    return False
                    break    

    return True
                    
val= input()
# passwords = ['abc', 'zxy', 'pqr']
val_split = input_val.split(" ")
passwords=[]
for i in range(len(passwords)):
    passwords.append(val_split[i])

    # print(password)

validPassword = checkPrefix(passwords)
# print("valid password:", validPassword)
if(validPassword):
    print("Good password ")
else:
    print("Bad password")