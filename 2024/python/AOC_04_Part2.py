class AOC_04_Part2:
    def __init__(self, fname):
        with open(fname, "r+") as contents:
            self.input_info = [item.split("\n")[0] for item in contents.readlines()]

    def check_bounds(self, index):
        if index < 0 or index >= self.rows:
            return 1
        else:
            return 0

    def check_mas(self, row_indx, col_indx, row_dir, col_dir):
        for item in "MAS":
            if self.input_info[row_indx][col_indx] != item:
                return 0
            row_indx += row_dir
            col_indx += col_dir
        return 1

    def check_x(self, row_indx, col_indx):
        counter = self.check_mas(
            col_indx + self.up, row_indx + self.left, self.down, self.right
        )
        counter += self.check_mas(
            col_indx + self.down, row_indx + self.left, self.up, self.right
        )
        counter += self.check_mas(
            col_indx + self.up, row_indx + self.right, self.down, self.left
        )
        counter += self.check_mas(
            col_indx + self.down, row_indx + self.right, self.up, self.left
        )
        if counter == 2:
            return 1
        else:
            return 0

    def main(self):
        self.rows = len(self.input_info)
        self.cols = len(self.input_info[0])
        self.straight = 0
        self.right = 1
        self.left = -1
        self.up = -1
        self.down = 1
        counter = 0
        for i in range(1, self.rows - 1):
            curr_row = self.input_info[i]
            for j in range(1, len(curr_row) - 1):
                counter += self.check_x(i, j)
        print(counter)


if __name__ == "__main__":
    init_class = AOC_04_Part2(fname="./04/input.txt")
    init_class.main()
