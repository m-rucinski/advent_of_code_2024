import sys

# sorry not sorry
sys.setrecursionlimit(100000)

room = [list(line.strip()) for line in open('aoc_d6_input.txt').readlines()]
size = len(room)
directions = ['^','>','v','<']
sum = 0


def walk(y,x,direction):
    #print("Walking on X=" + str(x) + " Y=" + str(y) + " Direction=" + str(direction))
    if direction == 1 and y-1 != -1 and room[y-1][x] != '#':
        if room[y-1][x] == '1':
            print("Trapped 1!")
            raise Exception()  
        room[y-1][x] = '1'
        walk(y-1, x, 1)
    elif direction == 1 and y-1 != -1 and room[y-1][x] == '#':
        walk(y,x,2)
    if direction == 2 and x+1 != size and room[y][x+1] != '#':
        if room[y][x+1] == '2':
            print("Trapped 2!")
            raise Exception()  
        room[y][x] = '2'
        walk(y, x+1, 2)
    elif direction == 2 and x+1 != size and room[y][x+1] == '#':
        walk(y,x,3)
    if direction == 3 and y+1 != size and room[y+1][x] != '#':
        if room[y+1][x] == '3':
            print("Trapped 3!")
            raise Exception()  
        room[y+1][x] = '3'
        walk(y+1, x, 3)
    elif direction == 3 and y+1 != size and room[y+1][x] == '#':
        walk(y,x,4)
    if direction == 4 and x-1 != -1 and room[y][x-1] != '#':
        if room[y][x-1] == '4':
            print("Trapped 4!")
            raise Exception()  
        room[y][x-1] = '4'
        walk(y, x-1, 4)
    elif direction == 4 and x-1 != -1 and room[y][x-1] == '#':
        walk(y,x,1)
    return 0

for i in range(size):
    try:
        #walk(i, room[i].index(directions[0]),1)
        startpos = [i, (room[i].index(directions[0]))]
    except ValueError:
        continue

for i in range(size):
    for j in range(size):
        room[i][j] = '#'
        try:
            if i == startpos[0] and j == startpos[1]:
                continue
            print('Starting at ' + str(i) + " and " + str(j))
            walk(startpos[0], startpos[1], 1)
        except:
            sum += 1 # lol
        room = [list(line.strip()) for line in open('aoc_d6_input.txt').readlines()]


print(sum)