from utils import load_file
from AOC_01_Part1 import clean_input


def main(fname):
    input_info = load_file(fname)
    list_1, list_2 = clean_input(input_info)
    total = 0
    for number in list_1:
        get_count_in_list2 = list_2.count(number)
        similarity = number * get_count_in_list2
        total += similarity
    print(f"The total similarity score is: ", total)


if __name__ == "__main__":
    main("./01/puzzle_input.txt")
