
def clumsyFactorial(n):
    operations=["*","/","+","-"]
    fact=""
    for i in range(n):
        fact+=str(n-i)
        if(i<n-1):
            fact+=operations[i%4]
        print(fact)
    return int(eval(fact))

# n=5
n=int(input())
print("factorial:", clumsyFactorial(n))