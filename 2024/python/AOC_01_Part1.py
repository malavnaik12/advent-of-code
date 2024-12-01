from utils import load_file


def clean_input(input_info):
    list_1 = []
    list_2 = []
    for item in input_info:
        row = item.split("\n")[0]
        row_numbers = [int(x) for x in row.split()]
        list_1.append(row_numbers[0])
        list_2.append(row_numbers[1])
    return list_1, list_2


def main(fname):
    input_info = load_file(fname)
    list_1, list_2 = clean_input(input_info)
    list_1.sort()
    list_2.sort()
    total = 0
    for num1, num2 in zip(list_1, list_2):
        total += abs(num1 - num2)
    print(f"Total Distance between lists: {total}")


if __name__ == "__main__":
    main("./01/puzzle_input.txt")
