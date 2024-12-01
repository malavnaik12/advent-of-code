def load_file(fname):
    with open(fname, "r+") as full_input:
        return full_input.readlines()
