def legoBlocks(height, width):
    MOD = (10**9 +7)

    # Step 1: O(W)      
    # The number of combinations to build a single row
    # As only four kinds of sizes, so
    # base case:
    # if width is 0, combination is 1
    # if width is 1, combination is 1
    # if width is 2, combination is 2
    # if width is 3, combination is 4
    singleRowLayouts = [1, 1, 2, 4]
   
    # Build row combinations up to current wall's width
    while len(singleRowLayouts) <= width:
        singleRowLayouts.append(sum(singleRowLayouts[-4:]) % MOD)
   
    print("singleRowLayouts", singleRowLayouts)


    # Step 2: O(W)
    # Compute total combinations
    # for constructing a wall of height N of varying widths
    # total = [pow(c, n, MOD) for c in row_combinations]
 
    totalLayouts=[]
    for w in singleRowLayouts:
        totalLayouts.append(pow(w, height, MOD))
   
    print("totalLayouts", totalLayouts)

   
    # Step 3: O(W^2)
    # Find the number of unstable wall configurations
    # for a wall of height N of varying widths
    unSolidLayouts = [0, 0]
   
    # Divide the wall into left part and right part,
    # and calculate the combination of left part and right part.
    # From width is 2, we start to consider about violation.
    for i in range(2, width + 1):
        # i: current total width
        # j: left width
        # i - j: right width
        # f: (left part - previous vertical violation)*right part
        f = lambda j: (totalLayouts[j] - unSolidLayouts[j]) * totalLayouts[i - j]
        result = sum(map(f, range(1, i)))
        unSolidLayouts.append(result % MOD)
   

    print("unsolid", unSolidLayouts)

    # Print the number of solid wall combinations
    return (totalLayouts[width] - unSolidLayouts[width]) % MOD

# print(legoBlocks(4,4))
height=int(input("enter the height"))
width=int(input("enter the width"))
output=legoBlocks(height, width)
print("no of combinations:", output)