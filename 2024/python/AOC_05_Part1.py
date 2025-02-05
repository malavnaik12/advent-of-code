with open("./05/test.txt", "r+") as fcontents:
    input_info = fcontents.readlines()

split_indx = input_info.index("\n")
rules = [item.split("\n")[0] for item in input_info[0:split_indx]]
printed_pages = [item.split("\n")[0] for item in input_info[split_indx + 1 :]]
print(split_indx, rules[0].split("|"), printed_pages)
