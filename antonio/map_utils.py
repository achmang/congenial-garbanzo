import os

path = "inputs/"

terrain_cost = {
    "#": 0,
    "~": 800,
    "*": 200,
    "+": 150,
    "X": 120,
    "_": 100,
    "H": 70,
    "T": 50
}

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
        "map_size": {
            "width":None,
            "height":None,
        },
        "office_count":None,
        "max_distance":None,
        "services":None,
        "building_costs":None,
        "offices":[{
            "x":None,
            "y":None,
            "points":None,
        }]
    }

    with open(path + file, "r") as f:
        # input values begin here
        lines = f.readlines()[0:8]
        for i, line in enumerate(lines):
            line = line.split()
            if i == 0:
                input_dict["map_size"]["width"] = int(line[0])
                input_dict["map_size"]["height"] = int(line[1])
                input_dict["office_count"] = int(line[2])
                input_dict["max_distance"] = int(line[3])
                input_dict["services"] = int(line[4])
            if i == 1:
                input_dict["building_costs"] = [int(string) for string in line]
            if i >= 2 and i <= 2+input_dict:
                return input_dict


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