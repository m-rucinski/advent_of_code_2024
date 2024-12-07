import re

matrix = [list(line.strip()) for line in open('aoc_d4_input.txt').readlines()]
target = ['M','S']

length = len(matrix)
result = 0

def check_index(x,y):
    if ((0 <= x < len(matrix)) and (0 <= y < len(matrix)) and matrix[x][y] != 'A' and matrix[x][y] != 'X'):
        return matrix[x][y]
    else:
        return 0

def search_xmas(x, y):
    global result

    # x-1, y+1 - up right
    # x+1, y-1 - down left
    # x-1, y-1 - up left
    # x+1, y+1 - down right
    
    val = check_index(x-1, y-1)
    if val != 0:
        print("Found " + val)
        val_c = check_index(x+1, y+1)
        if val_c == target[target.index(val) - 1]:
            print("Found " + val_c)
            val = check_index(x-1, y+1)
            if val != 0:
                print("Found " + val)
                val_c = check_index(x+1, y-1)
                if val_c == target[target.index(val) - 1]:
                    print("XMAS! Found " + val_c)
                    result +=1
                    return
    return 0

for i in range(length):
    for j in range(length):
        if matrix[i][j] == 'A':
            print("found A!")
            search_xmas(i,j)

print('Number of XMAS: ' + str(result))