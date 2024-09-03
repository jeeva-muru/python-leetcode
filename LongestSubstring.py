
#longest substring with no repeating characters 
def findLongestSubstrLength(letters):
    maxLength=0
    longestString=""

    for i in range(len(letters)):
       
        for j in range(i,len(letters)):
            subString = letters[i:j+1]
        # print(count)
            print(subString)
            print("set", set(subString))

            if (len(subString) == len(set(subString))):
                if (len(subString) > maxLength):
                    longestString = subString
                    maxLength = len(subString)

    return maxLength

#main
letters=input("enter the string:")
# longestString = findLength(letters)
print("length", findLongestSubstrLength(letters))



