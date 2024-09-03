# contiguous array with equal number of 0's and 1's
def findMaxLength(nums):
    max_length=0
    sum=0
    hash={}
    for i in range(len(nums)):
        current=nums[i]
        if current==0:
            sum-=1
        else:
            sum+=1
        if sum==0:
            max_length=i+1
        if sum in hash:
            max_length=max(max_length,i-hash[sum])
        else:
            hash[sum]=i
    return max_length

# Test cases
# nums1 = [0,0,0,1,1,1,1,0]

# nums1 =[0,1,0]
# print("The max length:",findMaxLength(nums1)) 


val=input()
val_split=val.split(",")
print(val_split)
nums=[]
for i in range(len(val_split)):
    nums.append(int(val_split[i]))
    print(nums)

print("Length:",findMaxLength(nums))   
   