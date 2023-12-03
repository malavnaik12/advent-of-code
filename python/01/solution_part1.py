"""
Advent of Code 2023: Challenge #1 Solution by Malav Naik
"""
## Solution Part 1 ##
f = open("input.txt", "r")
filelines = f.readlines()
total = 0
numbers = []
for line in filelines:
    elements = list(line)
    num_list_curr = []
    for element in elements:
        try:
            element_convert = int(element)
            num_list_curr.append(element_convert)
        except:
            continue
    current_num = int(f"{num_list_curr[0]}{num_list_curr[-1]}")
    numbers.append(current_num)
    total += current_num
print("total:",total)