"""
Advent of Code 2023: Challenge #3 Part 1 Solution by Malav Naik
"""
from string import punctuation
import numpy as np

class d3_p1:
    def __init__(self) -> None:
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.full_list = list(punctuation)
        self.punc_list = list(punctuation)
        period_index = self.full_list.index(".")
        self.full_list.pop(period_index)
        self.punc_list.pop(period_index)
        for item in self.numbers:
            self.full_list.append(item)
        self.f = open('input.txt','r')

    def main(self):
        # print(self.full_list)
        # input()
        schem_lines = self.f.readlines()
        trimmed_lines = []
        for line in schem_lines:
            trimmed_lines.append(list(line.split('\n')[0]))
            # print(trim)
            # input()
        trimmed_lines_arr = np.array(list(trimmed_lines))
        get_indx = np.isin(trimmed_lines_arr,self.full_list)
        print(trimmed_lines_arr,trimmed_lines_arr.shape)
        for ii in range(0,get_indx.shape[0]):
            temp = np.where(get_indx[ii,:]==True)[0]
            for col_id in temp:
                try:
                    if (trimmed_lines_arr[ii,col_id] in self.punc_list):
                        print(ii,col_id,trimmed_lines_arr[ii,col_id])
                except:
                    continue
            input()
        
if __name__ == "__main__":
    init = d3_p1()
    init.main()