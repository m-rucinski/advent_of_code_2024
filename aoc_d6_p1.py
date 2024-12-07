import sys

# sorry not sorry
sys.setrecursionlimit(10000)

room = [list(line.strip()) for line in open('aoc_d6_input.txt').readlines()]
size = len(room)
directions = ['^','>','v','<']
print(room)
sum = 0


def walk(y,x,direction):
    print("Walking on X=" + str(x) + " Y=" + str(y))
    if direction == 1 and y-1 != -1 and room[y-1][x] != '#':
        room[y-1][x] = 'X'
        walk(y-1, x, 1)
    elif direction == 1 and y-1 != -1 and room[y-1][x] == '#':
        print("turning!")
        walk(y,x,2)
    if direction == 2 and x+1 != size and room[y][x+1] != '#':
        room[y][x+1] = 'X'
        walk(y, x+1, 2)
    elif direction == 2 and x+1 != size and room[y][x+1] == '#':
        walk(y,x,3)
    if direction == 3 and y+1 != size and room[y+1][x] != '#':
        room[y+1][x] = 'X'
        walk(y+1, x, 3)
    elif direction == 3 and y+1 != size and room[y+1][x] == '#':
        walk(y,x,4)
    if direction == 4 and x-1 != -1 and room[y][x-1] != '#':
        room[y][x-1] = 'X'
        walk(y, x-1, 4)
    elif direction == 4 and x-1 != -1 and room[y][x-1] == '#':
        walk(y,x,1)
    return

for i in range(len(room)):
    try:
        walk(i, room[i].index(directions[0]),1)
    except ValueError:
        continue
print(room)
for i in range(len(room)):
    sum += room[i].count('X') + 1 # yeah 
print(sum)