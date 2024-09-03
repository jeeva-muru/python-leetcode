#function to find uppercase percentage in the given email
def findUpperCasePercentage(myEmail):
    upperCaseCount=0
    emailLength = len(myEmail)

    for c in myEmail:
        if c.isupper():
            upperCaseCount=upperCaseCount+1
    upperCasePercentage=round(upperCaseCount/emailLength*100,2)
    return upperCasePercentage

#function to find lowercase percentage in the given email
def findLowerCasePercentage(myEmail):
    lowerCaseCount=0

    emailLength = len(myEmail)

    for c in myEmail:
        if c.islower():
            lowerCaseCount=lowerCaseCount+1
    lowerCasePercentage=round(lowerCaseCount/emailLength*100,2)
    return lowerCasePercentage

#function to find digits percentage in the given email
def findDigitsPercentage(myEmail):
    digitsCount=0
    emailLength = len(myEmail)
    for c in myEmail:
        if c.isdigit():
            digitsCount=digitsCount+1
    digitsPercentage=round(digitsCount/emailLength*100,2)
    return digitsPercentage

#function to find other characters percentage in the given email
def findOtherCharactersPercentage(myEmail):
    othersCount=0
    emailLength = len(myEmail)
    for c in myEmail:
        if  ((not c.isupper()) and (not c.islower()) and (not c.isdigit()) ):
            othersCount=othersCount+1
    otherCharactersPercentage=round(othersCount/emailLength*100,2)
    return otherCharactersPercentage
    
#main
myEmail="eMail_Address321@anymail.com"
upperCasePercentage = findUpperCasePercentage(myEmail)
lowerCasePercentage = findLowerCasePercentage(myEmail)
digitsPercentage = findDigitsPercentage(myEmail)
otherCharactersPercentage = findOtherCharactersPercentage(myEmail)
print("Given Email: ",myEmail)
print(f"Uppercase letters: {upperCasePercentage}%")
print(f"Lowercase letters: {lowerCasePercentage}%")
print(f"Digits: {digitsPercentage}%")
print(f"Other characters: {otherCharactersPercentage}%")