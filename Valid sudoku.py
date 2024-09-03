import math


def findDuplicate(items):
    # print(row)
    digits = ["1", "2", "3", "4","5","6","7","8","9"]
    digitsCount = [0, 0, 0, 0,0,0,0,0,0]

    for i in range(len(items)):
        # print(row[i])
        for j in range(len(digits)):
            if (items[i] == digits[j]):

               digitsCount[int(items[i])-1] += 1
    
    # print("digits count:",digitsCount)

    for k in range(len(digitsCount)):
        if (digitsCount[k] > 1):
            return True

    return False

# def getBox(board, rowStart, colStart):
#     box=[]
#     start1 = rowStart
#     start2 = colStart
#     for start1 in range(start,start+3):
#         print(start1)
#         for start2 in range(3):
#             # print(board[i][j])
#             box.append(board[start1][start2])
#     print(box)
#     return box



#main
board1 = [["5","3",".",".","7",".",".",".","."]
        ,["6","6",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
board = board1
#board = board2

# row check
for i in range(len(board)):
    duplicate = findDuplicate(board[i])
    if (duplicate):
        break

# column check
col=[]
for j in range(len(board)):
    temp=[]
    for k in range(len(board)):
        temp.append(board[k][j])
    col.append(temp)

for i in range(len(col)):
    duplicate = findDuplicate(col[i])
    if (duplicate):
        break

if (duplicate):
    print("Col Not Valid")
else:
    print("Col Valid")

# 3x3 check
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        # print("start",start)
        box=[]
        for row in range(j, j + 3):
            for col in range(i, i + 3):
                # boxItems = getBox(row, col)  
                box.append(board[row][col]) 
        print(box)

        # # boxItems = getBox(board, start)
        duplicate = findDuplicate(box)
        # # boxItems=[]

        if(duplicate):
            print("Not valid")
        else:
            print("valid")


val=input()
val_split=val.split(" ")
print(val_split)
