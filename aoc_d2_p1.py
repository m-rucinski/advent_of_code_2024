import csv
import re

#finder = re.compile(r'(?P<first>\d+)[\s]{1}(?P<second>\d+)[\s]{1}(?P<third>\d+)[\s]{1}(?P<fourth>\d+)[\s]{1}(?P<fifth>\d+)')
finder = re.compile(r'\d+')
sum = 0

with open('aoc_d2_input.csv', 'r') as infile:
    counter = 0
    while True:
        counter +=1
        print("COUNTER: " + str(counter))
        content = infile.readline()
        if not content:
            break
        success = True
        list = [int(d) for d in finder.findall(content)]
        print(list)
        dir = list[0] - list[1]
        match dir:
            case 0:
                success = False
            case dir if dir > 0:
                dir = 1
            case dir if dir < 0:
                dir = -1
            case _:
                print('Something went wrong')
                exit
                
        print('direction is ' + str(dir))
        
        for el in range(len(list)-1):
            print('Comparing ' + str(list[el]) + ' and ' + str(list[el+1]) + '')
            diff = list[el] - list[el+1]
            if diff == 0:
                success = False
                break
            comp = (diff) / (abs(diff))

            print('difference = ' + str(abs(diff)))
            print('comp = ' + str(comp))
            if comp != dir or abs(diff) > 3:
                print('Does not fit')
                success = False
                break
        
        if success:
            sum += 1
    print(sum)
