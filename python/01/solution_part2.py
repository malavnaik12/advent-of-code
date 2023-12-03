"""
Advent of Code 2023: Challenge #1, Part #2 Solution by Malav Naik
"""
## Solution Part 2 ##
class d1_p2:
    def __init__(self) -> None:
        self.num_letters = {'one':1,'two':2,'thr':3,'fou':4,'fiv':5,'six':6,'sev':7,'eig':8,'nin':9}
        self.first_letters = set()
        self.second_letters = set()
        self.third_letters = set()
        for num in self.num_letters.keys():
            self.first_letters.update(list(num)[0])
            self.second_letters.update(list(num)[1])
            self.third_letters.update(list(num)[2])
        self.f = open("input.txt", "r")
    
    def main(self):
        filelines = self.f.readlines()
        total = 0
        numbers = []
        for line in filelines:
            elements = list(line)
            num_list_curr = []
            for ii in range(0,len(elements)):
                try:
                    element_convert = int(elements[ii])
                    num_list_curr.append(element_convert)
                except:
                    try:
                        if (elements[ii] in self.first_letters):
                            if ((elements[ii+1] in self.second_letters) and (elements[ii+2] in self.third_letters) and (ii < len(elements))):
                                number_letters = f"{elements[ii]}{elements[ii+1]}{elements[ii+2]}"
                                number = self.num_letters[number_letters]
                                num_list_curr.append(number)
                                ii+2
                    except:
                        continue
            current_num = int(f"{num_list_curr[0]}{num_list_curr[-1]}")
            numbers.append(current_num)
            total += current_num
        print("total:",total)

if __name__=="__main__":
    init = d1_p2()
    init.main()