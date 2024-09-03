# replace array with start index to end index with value
def arrayManipulate(array_size, queryArray):
    numArray=[0]*array_size
    # print(numArray)
    for i in range(len(queryArray)):
        num_split=queryArray[i].split(" ")
        startIndex=int(num_split[0])
        endIndex = int(num_split[1])
        value = int(num_split[2])
        # element = numArray[startIndex-1:endIndex]
        for j in range(startIndex-1, endIndex):
            numArray[j]+=value
        # print("start",startIndex)
        # print("end", endIndex)
        # print(numArray)

        # for i in range(len(element)):
            
        # print(sumArray)
    return max(numArray)       


array_size=int(input())
queryCount=int(input())
queryArray=[]
#start index, end index, value
for i in range(queryCount):
    numberPair=input()
    queryArray.append(numberPair)
# print(queryArray)

result = arrayManipulate(array_size, queryArray)
print("result:", result)