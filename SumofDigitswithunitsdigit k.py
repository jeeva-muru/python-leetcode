
def sumOfDigits(num,k):
    if(num==0):
        return 0
    
    
    for i in range(1, 11):
      if i * k % 10 == num % 10:
        return i

    return -1
        
# number = int(input("enter the number:"))
# k = int(input("enter the unit digit:"))
# print("The no of times:",sumOfDigits(number,k))

