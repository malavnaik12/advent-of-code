import re
import cupy as np

def find_location(seed_val,map_info,trunc_maps):
    indx = seed_val
    for key in map_info.keys():
        map_values = map_info[key]
        for ranges in map_values:        
            dest_start = ranges[0]
            source_start = ranges[1]
            length = ranges[2]
            replace_vals = np.arange(dest_start,dest_start+length)
            trunc_maps[source_start:source_start+length,1] = replace_vals
        next_indx = trunc_maps[indx,1]
        indx = next_indx
        trunc_maps[:,0] = trunc_maps[:,1]
        trunc_maps[:,1] = np.arange(0,max_value)
        if key == 'humidity-to-location':
            location = next_indx
    return location

f = open('input.txt', 'r')
root = [re.split(r'\s{1,}',line) for line in f.readlines()]
maps = [line[:-1] if line[-1] == '' else line for line in root]
seeds = [int(number) for number in maps[0][1:]]
info = [line for line in maps[2:] if ((len(line) >= 1) and (line[0] != ''))]
title_indx = []
map_info = {}
count = 0
for ii in range(0,len(info)):
    try:
        int(info[ii][0])
    except ValueError:
        title_indx.append(ii)
for indx, num in enumerate(title_indx):
    if info[num][0] == 'end-doc':
        break
    map_info[info[num][0]] = [[int(number) for number in item] for item in info[num+1:title_indx[indx+1]]]
max_value = 1000000000
trunc_maps = np.tile(np.arange(0,max_value).reshape(max_value,1),(1,2))
locations = []
for seed in seeds:
    loc = find_location(seed,map_info,trunc_maps)
    locations.append(loc)
print(f"Minimum Location: {min(locations)}\nLocations: {locations}")

# for ii in range(0,len(map_info.keys())):
#     key = list(map_info.keys())[ii]
#     map_values = map_info[key]
#     colm = ii+1
#     for ranges in map_values:
#         dest_start = ranges[0]
#         source_start = ranges[1]
#         length = ranges[2]
#         replace_vals = np.arange(dest_start,dest_start+length)
#         all_maps[source_start:source_start+length,colm] = replace_vals

# locations = []
# for seed in seeds:
#     soil = all_maps[seed,1]
#     fertilizer = all_maps[soil,2]
#     water = all_maps[fertilizer,3]
#     light = all_maps[water,4]
#     temperature = all_maps[light,5]
#     humidity = all_maps[temperature,6]
#     location = all_maps[humidity,7]
#     locations.append(location)
# print(f"Minimum Location: {min(locations)}\nLocations: {locations}")
