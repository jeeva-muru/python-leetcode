import math
def egyptianFraction(numerator, denominator):
    fractions=[]

    while(numerator!=0):
        x=math.ceil(denominator/numerator)
        fractions.append(x)
        numerator=x*numerator-denominator
        denominator=x*denominator

    for i in range(len(fractions)):
        print(fractions[i])

egyptianFraction(6,14)



	
