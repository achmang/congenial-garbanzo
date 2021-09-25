import os

path = "inputs/"

def inputs_to_dict(file):
    # init the struct, make it easier
    input_dict = {
        "map_size": {
            "width":None,
            "height":None,
        },
        "office_count":None,
        "max_distance":None,
        "services":None,
        "building_costs":None,
        "office_params":[],
        "service_params":[]
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
            # set the boundry for office params
            if i >= 2 and i < 2 + input_dict["office_count"]:
                input_dict["office_params"].append({
                    "x": int(line[0]),
                    "y": int(line[1]),
                    "cost": int(line[2])
                })
            # anything after this is service related
            if i >= 2 + input_dict["office_count"]:
                input_dict["service_params"].append({
                    "x": int(line[0]),
                    "y": int(line[1]),
                    "utility": int(line[2])
                })

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

def map_lookup(x, y, map):
    try:
        return map[x][y]
    except:
        print("out of bounds")

def validate_map_size(width, height, map_arr):
    if height > 2000 or height < 1:
        return False

    if width > 2000 or width < 1:
        return False

    if height != len(map_arr):
        return False
    
    for row in map_arr:
        if width != len(row):
            return False

    return True

def validate_inputs(inputs_dict):
    # check that these match the actual values.
    office_count = inputs_dict["office_count"]
    service_count = inputs_dict["services"]

    if len(inputs_dict["office_params"]) != office_count:
        return False
    if len(inputs_dict["service_params"]) != service_count:
        return False
    if inputs_dict["max_distance"] > 2000 or inputs_dict["max_distance"] < 1:
        return False
    if office_count > 500 or office_count < 1:
        return False
    
    return True

# def validate_solution(solution):

# def validate_offices(map_arr, input_dict):
#     # check that reply offices are in a valid location
#     try:
#         for i, row in map_arr:
#             if row
#     except


if __name__ == "__main__":
    all_files = os.listdir(path)
    for file in all_files:
       inputs_dict = inputs_to_dict(file)
        if not validate_inputs(inputs_dict):
           print("inputs not valid")
           continue
        if not validate_map_size(inputs_dict["map_size"]["width"], inputs_dict["map_size"]["height"]):
            print("inputs not valid")
            continue
