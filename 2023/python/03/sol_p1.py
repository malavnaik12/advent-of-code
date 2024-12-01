import numpy as np
import string
import re

numbers = list(string.digits)
punc_list = list(string.punctuation)
period_index = list(punc_list).index(".")
punc_list.pop(period_index)
f = open('test.txt','r')
slider = [-1,0,1]
schem_lines = f.readlines()
trimmed_lines = []
for line in schem_lines:
    trimmed_lines.append(list(line.split('\n')[0]))
trimmed_lines_arr = np.array(list(trimmed_lines))
special_char_indx = np.isin(trimmed_lines_arr,punc_list)
special_char_loc = np.argwhere(special_char_indx==True)
num_indx = np.argwhere(np.isin(trimmed_lines_arr,numbers)==True)
num_loc = list(map(tuple,num_indx))
print(special_char_loc)
for loc in special_char_loc:
    x_char = loc[0]; y_char = loc[1]
    print(x_char,y_char)
    x_window = list(map(int,x_char+slider)); y_window = list(map(int,y_char+slider))
    window_locs = []
    for x in x_window:
        for y in y_window:
            window_locs.append(tuple([x,y]))
    print(x_window,y_window,window_locs)
    assess_mat = np.ravel(trimmed_lines_arr[x_window[0]:x_window[-1]+1,y_window[0]:y_window[-1]+1])
    print(assess_mat)
    loc_numbers_window = list(map(int,np.ravel(np.argwhere(np.isin(assess_mat,numbers)==True))))
    for num_loc in loc_numbers_window:
        print(window_locs[num_loc])
    input()