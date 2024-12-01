import re

class part_sol:
    def __init__(self) -> None:
        f = open('input.txt','r')
        lines = [line.split('\n')[0] for line in f.readlines()]
        self.total = 0
        self.info_dict = {}
        self.card_counts = {}
        for ii in range(0,len(lines)):
            data = lines[ii]
            self.info_dict[data.split(':')[0]] = data.split(':')[1]
            self.card_counts[data.split(':')[0]] = 1
    
    def part1_ops(self,num_list):
        test_strings = re.split(r'\s{1,}',num_list[0])
        bank_strings = re.split(r'\s{1,}',num_list[1])
        
        test_nums = []
        for string in test_strings:
            try:
                test_nums.append(int(string))
            except:
                continue
        self.overlap_nums = 0
        for string in bank_strings:
            try:
                if (int(string) in test_nums):
                    self.overlap_nums += 1
            except:
                continue

    def part2_ops(self,key):
        data = self.info_dict[key]
        card_num = int(re.split(r'\s{1,}',key)[1])
        numbers = data.split('|')
        self.part1_ops(numbers)
        for jj in range(card_num+1,card_num+1+self.overlap_nums):
            if (jj <= 9):
                space = '  '
            elif ((jj > 9) and (jj <= 99)):
                space = ' '
            else:
                space = ''
            self.card_counts[f"Card {space}{jj}"] += 1

    def main(self):
        for key in self.card_counts.keys():
            print(f"{key}:{self.card_counts[key]}")
            for _ in range(0,self.card_counts[key]):
                self.part2_ops(key)
            self.total += self.card_counts[key]
        print(self.total)

if __name__ == "__main__":
    init_class = part_sol()
    init_class.main()