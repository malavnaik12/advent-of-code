"""
Advent of Code 2023: Challenge #2, Part 1 Solution by Malav Naik
"""
class d2_p1:
    def __init__(self) -> None:
        self.max_values = {'red':12,'green':13,'blue':14}
        self.f = open('input.txt','r')

    def main(self):
        games = self.f.readlines()
        total = 0
        for game_info in games:
            game_trim = game_info.split('\n')
            all_games = game_trim[0].split(":")
            game_id = int(all_games[0].split(' ')[1])
            ind_games = all_games[1].split(";")
            game_check_count = 0
            for game in ind_games:
                game_entries = game.split(',')
                entry_check_count = 0
                for entry in game_entries:
                    entry_pair = entry.split(' ')[1:]
                    entry_pair_number = entry_pair[0]
                    entry_pair_colour = entry_pair[-1]
                    if (int(entry_pair_number) <= self.max_values[entry_pair_colour]):
                        entry_check_count += 1
                if (entry_check_count == len(game_entries)):
                    game_check_count += 1
            if (game_check_count == len(ind_games)):
                total += game_id
            else:
                continue
        print("total:", total)

if __name__ == "__main__":
    init = d2_p1()
    init.main()