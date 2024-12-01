import re
f = open('input.txt','r').readlines()
data = [line.split(":") for line in f]
info = []
for line in data:
    num_str = ''
    for string in line[1]:
        try:
            int(string)
            num_str += string
        except:
            continue
    info.append(int(num_str))
count = 0
for ii in range(0,info[0]):
    hold_time = ii
    travel_time = info[0] - ii
    distance = hold_time*travel_time
    if (distance > info[1]):
        count += 1
print(count)