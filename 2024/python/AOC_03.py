import re


def get_regex_result(regex_string, result):
    regex_result = re.findall(
        r"mul\((\d+),(\d+)\)",
        regex_string,
        # r"do\(\)[\w$&+,:;=?@#|'<>.-^*()%!]mul\((\d{1,3}),(\d{1,3})\)", list_item
    )
    for item in regex_result:
        result += int(item[0]) * int(item[1])
    return result


def main(fname, ques):
    result = 0
    file = open(fname)
    input_info = str(file.read())
    if ques == 2:
        do_split = input_info.split("do()")
        for sublist in do_split:
            dont_split = sublist.split("don't()")[0]
            result = get_regex_result(dont_split, result)
    else:
        result = get_regex_result(input_info, result)
    print("Result:", result)


if __name__ == "__main__":
    main("./03/input.txt", 2)
