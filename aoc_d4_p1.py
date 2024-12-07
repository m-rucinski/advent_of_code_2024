import re

matrix = [list(line.strip()) for line in open('aoc_d4_input.txt').readlines()]
target = ['X','M','A','S']

length = len(matrix)
result = 0

def check_index(x,y):
    if (0 <= x < len(matrix)) and (0 <= y < len(matrix)):
        return True
    else:
        return False

def search_xmas(x, y, target_char, direction):
    global result
    if target_char == 4:
        print("FOUND XMAS!")
        result +=1
        return
    if (direction == 0 or direction == 1) and check_index(x,y+target_char) and matrix[x][y+target_char] == target[target_char]:
        print("found " + target[target_char] + " right")
        search_xmas(x,y,target_char+1, 1)
    if (direction == 0 or direction == 2) and check_index(x+target_char,y+target_char) and matrix[x+target_char][y+target_char] == target[target_char]:
        print("found " + target[target_char] + " down right")
        search_xmas(x,y,target_char+1, 2)
    if (direction == 0 or direction == 3) and check_index(x+target_char,y) and matrix[x+target_char][y] == target[target_char]:
        print("found " + target[target_char] + " down")
        search_xmas(x,y,target_char+1, 3)
    if (direction == 0 or direction == 4) and check_index(x+target_char,y-target_char) and matrix[x+target_char][y-target_char] == target[target_char]:
        print("found " + target[target_char] + " down left")
        search_xmas(x,y,target_char+1, 4)
    if (direction == 0 or direction == 5) and check_index(x,y-target_char) and matrix[x][y-target_char] == target[target_char]:
        print("found " + target[target_char] + " left")
        search_xmas(x,y,target_char+1, 5)
    if (direction == 0 or direction == 6) and check_index(x-target_char,y-target_char) and matrix[x-target_char][y-target_char] == target[target_char]:
        print("found " + target[target_char] + " up left")
        search_xmas(x,y,target_char+1, 6)
    if (direction == 0 or direction == 7) and check_index(x-target_char,y) and matrix[x-target_char][y] == target[target_char]:
        print("found " + target[target_char] + " up")
        search_xmas(x,y,target_char+1, 7)
    if (direction == 0 or direction == 8) and check_index(x-target_char,y+target_char) and matrix[x-target_char][y+target_char] == target[target_char]:
        print("found " + target[target_char] + " up right")
        search_xmas(x,y,target_char+1, 8)
    return 0


for i in range(length):
    for j in range(length):
        if matrix[i][j] == 'X':
            print("found X!")
            search_xmas(i,j,1,0)

print('Number of XMAS: ' + str(result))