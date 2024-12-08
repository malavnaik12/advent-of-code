class AOC_04_Part1:
    def __init__(self, fname):
        with open(fname, "r+") as contents:
            self.input_info = [item.split("\n")[0] for item in contents.readlines()]

    def check_bounds(self, index):
        if index < 0 or index >= self.rows:
            return 1
        else:
            return 0

    def check_xmas(self, row_indx, col_indx, row_dir, col_dir):
        for item in "XMAS":
            if self.check_bounds(row_indx):
                return 0
            elif self.check_bounds(col_indx):
                return 0
            elif self.input_info[row_indx][col_indx] != item:
                return 0
            row_indx += row_dir
            col_indx += col_dir
        return 1

    def main(self):
        self.rows = len(self.input_info)
        self.cols = len(self.input_info[0])
        straight = 0
        right = 1
        left = -1
        up = -1
        down = 1
        counter = 0
        for i in range(0, self.rows):
            curr_row = self.input_info[i]
            if self.check_bounds(i):
                continue
            else:
                for j in range(0, len(curr_row)):
                    if self.check_bounds(j):
                        continue
                    else:
                        counter += self.check_xmas(i, j, straight, right)
                        counter += self.check_xmas(i, j, straight, left)
                        counter += self.check_xmas(i, j, down, straight)
                        counter += self.check_xmas(i, j, up, straight)
                        counter += self.check_xmas(i, j, left, up)
                        counter += self.check_xmas(i, j, left, down)
                        counter += self.check_xmas(i, j, right, up)
                        counter += self.check_xmas(i, j, right, down)
        print(counter)


if __name__ == "__main__":
    init_class = AOC_04_Part1(fname="./04/input.txt")
    init_class.main()
