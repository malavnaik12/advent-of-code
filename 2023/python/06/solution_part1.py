import re
import numpy as np
f = open('input.txt','r').readlines()
data = [re.split(r'\s{1,}',line) for line in f]
info_dict = {
            data[0][0][0:4]:[int(number) for number in data[0][1:] if number != ''],
            data[1][0][0:8]:[int(number) for number in data[1][1:] if number != '']}
better_dist = []
multi_dist = 1
for race in range(0,len(info_dict['Time'])):
    count = 0
    time = info_dict['Time'][race]
    record_dist = info_dict['Distance'][race]
    for ii in range(0,time):
        hold_time = ii
        travel_time = time - ii
        distance = hold_time*travel_time
        if (distance > record_dist):
            count += 1
    better_dist.append(count)
    multi_dist = multi_dist*count
print(better_dist,multi_dist)