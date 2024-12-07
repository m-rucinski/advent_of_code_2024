import csv
import re

#finder = re.compile(r'(?P<first>\d+)[\s]{1}(?P<second>\d+)[\s]{1}(?P<third>\d+)[\s]{1}(?P<fourth>\d+)[\s]{1}(?P<fifth>\d+)')
finder = re.compile(r'\d+')
sum = 0

def is_safe(list):
    print(list)
    success = True
    dir = list[0] - list[1]
    match dir:
        case dir if dir > 0:
            dir = 1
        case dir if dir < 0:
            dir = -1
        case _:
            print('IS ZERO')
            
    print('direction is ' + str(dir))
    
    for el in range(len(list)-1):
        print('Comparing ' + str(list[el]) + ' and ' + str(list[el+1]) + '')
        diff = list[el] - list[el+1]
        if diff == 0:
            print('Does not fit')
            success = False
            comp = 0
        else:
            comp = (diff) / (abs(diff))

        print('difference = ' + str(abs(diff)))
        print('comp = ' + str(comp))
        if comp != dir or abs(diff) > 3:
            print('Does not fit')
            success = False
        
    return success
    

with open('aoc_d2_input.csv', 'r') as infile:
    counter = 0
    while True:
        counter +=1
        content = infile.readline()
        if not content:
            break
        list = [int(d) for d in finder.findall(content)]
        if is_safe(list):
            sum += 1
        else:
            for i in range(len(list)):
                new_list = list.copy()
                print('NEW LIST:' + str(i) + ' - '  + str(new_list))
                new_list.pop(i)
                if is_safe(new_list):
                    sum += 1
                    break

    print(sum)
