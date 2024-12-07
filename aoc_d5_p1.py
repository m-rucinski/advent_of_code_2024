import re 

rules = [list(re.findall('\d+',line)) for line in open('aoc_d5_input_rules.txt').readlines()]
updates = [list(re.findall('\d+',line)) for line in open('aoc_d5_input.txt').readlines()]

sum = 0

for i in range(len(updates)):
    print(updates[i])
    success = True
    for j in range(len(rules)):
        try:
            if updates[i].index(rules[j][0]) > updates[i].index(rules[j][1]):
                print('breaking!')
                success = False
                break
        except ValueError:
            continue
    if(success):
        sum+=int(updates[i][int((len(updates[i]) + 1) / 2 - 1)])
        print('current sum: ' + str(sum))

print(sum)