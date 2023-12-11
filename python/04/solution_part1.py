import re

def extract_card_total(num_list):
    test_strings = re.split(r'\s{1,}',num_list[0])
    test_nums = []
    for string in test_strings:
        try:
            test_nums.append(int(string))
        except:
            continue
    bank_strings = re.split(r'\s{1,}',num_list[1])
    count = 0
    for string in bank_strings:
        try:
            if (int(string) in test_nums):
                count += 1
        except:
            continue
    if count == 0:
        card_total = 0
    else:
        card_total = 2**(count-1)
    return card_total

f = open('input.txt','r')
lines = [line.split('\n')[0] for line in f.readlines()]
total = 0
for card in lines:
    numbers = card.split(':')[1].split('|')
    card_total = extract_card_total(numbers)
    total += card_total
print(total)