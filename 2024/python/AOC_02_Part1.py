from utils import load_file


def clean_item(item):
    return [int(x) for x in item.split("\n")[0].split()]


def get_sign(item):
    return 1 if item >= 0 else -1


def main(fname):
    input_info = load_file(fname)
    safe_count = 0
    for item in input_info:
        level = clean_item(item)
        if len(set(level)) != len(level):
            continue
        else:
            sub_count = 0
            expected_sign = get_sign(level[-1] - level[0])
            for ii in range(1, len(level)):
                diff = level[ii] - level[ii - 1]
                if abs(diff) not in [1, 2, 3]:
                    break
                else:
                    if get_sign(diff) != expected_sign:
                        break
                    else:
                        expected_sign = get_sign(diff)
                        sub_count += 1
            if sub_count + 1 == len(level):
                safe_count += 1
    print(f"Number of Safe Reports: {safe_count}")


if __name__ == "__main__":
    main("./02/puzzle_input.txt")
