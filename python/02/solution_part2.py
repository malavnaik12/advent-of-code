"""
Advent of Code 2023: Challenge #2, Part 2 Solution by Malav Naik
"""
class d2_p2:
    def __init__(self) -> None:
        self.f = open('input.txt','r')

    def main(self):
        games = self.f.readlines()
        total = 0
        for game_info in games:
            self.min_values = {'red':0,'green':0,'blue':0}
            game_trim = game_info.split('\n')
            all_games = game_trim[0].split(":")
            ind_games = all_games[1].split(";")
            for game in ind_games:
                game_entries = game.split(',')
                entry_check_count = 0
                for entry in game_entries:
                    entry_pair = entry.split(' ')[1:]
                    entry_pair_number = entry_pair[0]
                    entry_pair_colour = entry_pair[-1]
                    if (int(entry_pair_number) >= self.min_values[entry_pair_colour]):
                        self.min_values[entry_pair_colour] = int(entry_pair_number)
            values = list(self.min_values.values())
            product = values[0]*values[1]*values[2]
            total += product
        print(total)

if __name__ == "__main__":
    init = d2_p2()
    init.main()