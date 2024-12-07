import csv
import re

a_list = []
b_list = []
finder = re.compile(r'(?P<first>\d+)[\s]{3}(?P<second>\d+)')
finder2 = re.compile(r'(?P<first>\d+)')
sum = 0


with open('aoc_d1_input.csv', 'r') as infile:
    counter = 0
    while True:
        counter +=1
        content = infile.readline()
        if not content:
            break
        
        a = int(finder.search(content).group('first'))
        b = int(finder.search(content).group('second'))
        a_list.append(a)
        b_list.append(b)
    
    for el in range(len(a_list)):
        same = b_list.count(a_list[el])
        print("same = " + str(same))
        sum += (a_list[el] * same)
    print(sum)
