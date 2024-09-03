#Query Kth smallest Trimmed Number
def findLowest(position, trimArray):
    arr = trimArray.copy()
    arr.sort()
    # print("sort arr", arr)
    return(arr[position-1])


def trimmedNumber(queryArray, nums):
    # nums=[]

    resultArray=[]
    for i in range(len(queryArray)):
        query_split=queryArray[i].split(" ")
        position = int(query_split[0])
        # print("position:",position)
        digits = int(query_split[1])
        # print("digits:", digits)
        trimArray=[]
        for j in range(len(nums)):
            # print(nums[j])
            element = nums[j][-(digits):]
            # print(element)
            trimArray.append(element)
        print("trim:", trimArray)
        
        
        lowest = findLowest(position, trimArray)
        # print("trim:", trimArray)
        index = trimArray.index(lowest)
        # print("index",index)
        resultArray.append(index)
        
    return resultArray 
        
# nums=["113","933","231","719"]
#nums=["123","456","246","369"]
numbers=input()
numbers_split=numbers.split(" ")
nums=[]
for i in range(len(numbers_split)):
    nums_val = numbers_split[i]
    nums.append(nums_val)

queryCount=int(input())
queryArray=[]

for i in range(queryCount):
    queryPair=input()
    queryArray.append(queryPair)
    # for j in range(len(queryPair_split1)):
    #     for k in range(len(queryPair_split2)):

# print("query array:", queryArray)

resultArray = trimmedNumber(queryArray, nums)
# print("result:",resultArray)
for i in range(len(resultArray)):
    print(resultArray[i], end=" ")