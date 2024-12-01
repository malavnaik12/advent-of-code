"""
Advent of Code 2023: Challenge #3 Part 1 Solution by Malav Naik
"""
import string
import numpy as np

class d3_p1:
    def __init__(self) -> None:
        self.numbers = list(string.digits)
        period_index = list(string.punctuation).index(".")
        self.punc_list = list(string.punctuation)
        self.punc_list.pop(period_index)
        self.f = open('input.txt','r')

    def main(self):
        schem_lines = self.f.readlines()
        trimmed_lines = []
        total = 0
        for line in schem_lines:
            trimmed_lines.append(list(line.split('\n')[0]))
        trimmed_lines_arr = np.array(list(trimmed_lines))
        special_char_indx = np.isin(trimmed_lines_arr,self.punc_list)
        special_char_loc = np.argwhere(special_char_indx==True)
        num_indx = np.argwhere(np.isin(trimmed_lines_arr,self.numbers)==True)
        num_loc = list(map(tuple,num_indx))
        assessed_num_coords = []
        for ii in range(0,len(special_char_loc)):
            x_coord = special_char_loc[ii][0]; y_coord = special_char_loc[ii][1]
            print(x_coord,y_coord)
            x_range = [x_coord-1,x_coord,x_coord+1,x_coord+2]
            y_range = [y_coord-1,y_coord,y_coord+1,y_coord+2]
            print(x_range,y_range)
            assess_mat = trimmed_lines_arr[x_coord-1:x_coord+2,y_coord-1:y_coord+2]
            print(assess_mat)
            find_number_loc = list(map(tuple,np.argwhere(np.isin(assess_mat,self.numbers)==True)))
            print(find_number_loc)
            number_coords = []
            for local_coords in find_number_loc:
                num_x = local_coords[0]; num_y = local_coords[1]
                number_coord = tuple([x_range[num_x],y_range[num_y]])
                assert (number_coord in num_loc)
                number_coords.append(number_coord)
                # print(coords, num_loc[0:10],coords in num_loc)
                print(number_coords)
                print(number_coord,num_loc[6],number_coord in num_loc)
            input()
            temp_dict = {'0':[],'1':[],'2':[]}
            for ii in range(0,len(find_number_loc)):
                x = x_range[find_number_loc[ii][0]]
                y = y_range[find_number_loc[ii][1]]
                temp_dict[str(x)].append(y)
            numbers_window = []
            for key in temp_dict.keys():
                y_vals = temp_dict[key]
                print(key,y_vals)
                # print(y_vals,y_range[1:3],y_vals==y_range[1:3])
                if len(y_vals) != 0:
                    if ((key != 1)):
                        if (y_vals == y_range[0:3]):
                            number = trimmed_lines_arr[int(key)][y_vals[0]:y_vals[-1]+1]
                        elif (y_vals == y_range[0:2]):
                            number = trimmed_lines_arr[int(key)][y_vals[0]-1:y_vals[-1]+1]
                        elif (y_vals == y_range[1:3]):
                            number = trimmed_lines_arr[int(key)][y_vals[0]:y_vals[-1]+2]
                    if (len(y_vals) == 1):
                        if (y_vals == y_range[0]):
                            number = trimmed_lines_arr[int(key)][y_vals[0]-1:y_vals[-1]+1]
                        elif (y_vals == y_range[2]):
                            number = trimmed_lines_arr[int(key)][y_vals[0]:y_vals[-1]+2]
                number_list = list(map(str,number))
                print(number_list)
                number_string = ''
                for ii in range(0,len(number_list)):
                    number_string += number_list[ii]
                print(type(number_string))
                number_int = int(number_string)
                    # int(f"{number_list[0]}{number_list[1]}{number_list[2]}")
                numbers_window.append(number_int)
            for num in numbers_window:
                total += num
        print(total)
        
if __name__ == "__main__":
    init = d3_p1()
    init.main()