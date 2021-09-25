import os

path = "inputs/"

def validate_input(file):
    # only txt files are valid
    if file.endswith(".txt"):
        with open(path + file, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
            # the first 8 lines are just input values
                if i >= 8:
                    break
        return True

def inputs_to_dict(file):

    input_dict = {

    }

    with open(path + file, "r") as f:
        # map starts at this part
        lines = f.readlines()[:8]
        for line in lines:
            # remove the new line
            line = line[:len(line)-1]

def map_to_array(file):
    map_arr = []
    with open(path + file, "r") as f:
        # map starts at this part
        lines = f.readlines()[8:]
        for line in lines:
            # remove the new line char '/n'
            line = line[:len(line)-1]
            map_arr.append(list(line))

    return map_arr


if __name__ == "__main__":
    all_files = os.listdir(path)
    print(all_files)
    for file in all_files:
        print(map_to_array(file))
