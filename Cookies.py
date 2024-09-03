
def cookies(candies):
    # candies=[]
    candies.sort()
    
    print(candies)
    step=0
    for i in range(len(candies)):
    
        leastCandy=candies.pop(0)
        # print(candies)
        secondLeastCandy=candies.pop(0)
        # print(candies)
        sweetness=leastCandy+2*secondLeastCandy
        # print(sweetness)
       
        # print(candies)
        step+=1
        if(candies[0] >= target):
            break

        candies.insert(0,sweetness)
        candies.sort()
        
    return step

candies = input()
target = int(input())
candies_split=candies.split(" ")
candies=[]
for i in range(len(candies_split)):
    candies.append(int(candies_split[i]))

print("steps:", cookies(candies))
