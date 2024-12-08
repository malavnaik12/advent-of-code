from utils import load_file
import numpy as np


def get_sign(item):
    return 1 if item > 0 else -1


def main(fname):
    input_info = load_file(fname)
    safe_count = 0
    for item in input_info:
        level = [int(x) for x in item.split("\n")[0].split()]
        if abs(len(set(level)) - len(level)) > 1:
            continue
        else:
            print(level)
            sub_count = 1
            popcount = 0
            expected_sign = get_sign(level[-1] - level[0])
            if expected_sign == 0:
                level.pop(-1)
                expected_sign = get_sign(level[-1] - level[0])
                popcount = 1
            ii = 0
            while ii < len(level):
                ii += 1
                diff = level[ii] - level[ii - 1]
                if abs(diff) not in [1, 2, 3]:
                    if popcount == 0:
                        level.pop(ii - 1)
                        ii -= 1
                        popcount = 1
                    else:
                        break
                else:
                    if get_sign(diff) != expected_sign:
                        if popcount == 0:
                            level.pop(ii - 1)
                            ii -= 1
                            popcount = 1
                        else:
                            break
                    else:
                        expected_sign = get_sign(diff)
                        sub_count += 1
                if sub_count == len(level):
                    safe_count += 1
                    break

    print(f"Number of Safe Reports: {safe_count}")


if __name__ == "__main__":
    main("./02/puzzle_input.txt")
