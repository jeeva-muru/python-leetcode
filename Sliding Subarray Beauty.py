def subarray(subarray_length, position, arr):
    subArr=[]
    for i in range(len(arr)):
    # start=arr[0]
    # end=arr[subarray_length]
    
    
        array_slice = arr[i:subarray_length+i]
        if(len(array_slice)!=subarray_length):
            break

        arrayPosition=array_slice[position-1]
        subArr.append(arrayPosition)
    
    # print("index",i)
    # print("array", array_slice)
    return subArr
# inputs
# 


subarray_length=int(input())
position=int(input())
arr=input()
arr_split=arr.split(" ")
arr=[]
for i in range(len(arr_split)):
    arr_val=int(arr_split[i])
    arr.append(arr_val)

result = subarray(subarray_length, position, arr)
for i in range(len(result)):
    print(result[i],end=" ")


    
