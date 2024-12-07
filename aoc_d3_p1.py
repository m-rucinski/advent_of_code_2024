import re

input = open('aoc_d3_input.txt').read()
print(input)
#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

sum = 0
input = input.replace('\r', '').replace('\n', '')
split_reg = re.compile(r"don't\(\).*?do\(\)")
input = "".join(str(s) for s in split_reg.split(input))
#print(input)
reg = re.compile(r'mul\((?P<v1>\d{1,3}),(?P<v2>\d{1,3})\)')
result = reg.findall(input)
#int_result = [int(d) for d in result]
#print(result)
for res in result:
    sum += (int(res[0]) * int(res[1]))
print(sum)