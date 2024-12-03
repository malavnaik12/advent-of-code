from utils import load_file
import numpy as np


def get_sign(item):
    return 1 if item > 0 else -1


def main(fname):
    input_info = load_file(fname)
    safe_count = 0
    for indx, item in enumerate(input_info):
        level = [int(x) for x in item.split("\n")[0].split()]
        if abs(len(set(level)) - len(level)) > 1:
            continue
        else:
            ii = 1
            sub_count = 1
            popped = False
            if level[-1] - level[0] == 0:
                level.pop(0)
                popped = True
                expected_sign = get_sign(level[-1] - level[0])
            else:
                expected_sign = get_sign(level[-1] - level[0])
            while ii < len(level):
                diff = level[ii] - level[ii - 1]
                if abs(diff) in [1, 2, 3]:
                    if get_sign(diff) == expected_sign:
                        sub_count += 1
                        ii += 1
                    else:
                        if not popped:
                            level.pop(ii - 1)
                            popped = True
                            if np.nansum(np.abs(np.diff(level)) > 3):
                                break
                        else:
                            break
                else:
                    if not popped:
                        level.pop(ii - 1)
                        popped = True
                        if np.nansum(np.abs(np.diff(level)) > 3):
                            break
                    else:
                        break
            print(indx, level, sub_count, len(level), safe_count)
            if sub_count == len(level):
                safe_count += 1

    print(f"Number of Safe Reports: {safe_count}")


if __name__ == "__main__":
    main("./02/puzzle_input.txt")
