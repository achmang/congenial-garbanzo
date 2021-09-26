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
            if(line[-1] =='\n'):
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

# this int finshed 
def validate_solution(solution, map_arr):

    test_string = "URRRRRUUURRRRDRRRRU"
    test_string = test_string.split()

    x = 2
    y = 5

    for i, char in enumerate(test_string):
        if char == "U":
            try:
                x += -1
                if map_arr[x][y] == "#":
                    return False
            except:
                print("solution invalid, out of bounds")
                return False
        if char == "D":
            try:
                x += 1
                if map_arr[x][y] == "#":
                    return False
            except:
                print("solution invalid, out of bounds")
                return
        if char == "L":
            try:
                y += -1
                if map_arr[x][y] == "#":
                    return False
            except:
                print("solution invalid, out of bounds")
                return False
        if char == "R":
            try:
                y+= 1
                if map_arr[x][y] == "#":
                    return False
            except:
                print("solution invalid, out of bounds")
                return False
        

def validate_offices(map_arr, input_dict):
    for office in input_dict["office_params"]:
        try:
            if map_lookup(office["x"], office["y"], map_arr) == "#":
                return False
        except:
            print("")
    
    return True
    
def map_lookup(x, y, map_arr):
    try:
        return map_arr[x][y]
    except:
        print("out of bounds " + str(x) + " " + str(y))


if __name__ == "__main__":
    all_files = os.listdir(path)
    for file in all_files:
        inputs_dict = inputs_to_dict(file)
        if not validate_inputs(inputs_dict):
            print("inputs not valid")
            continue

        map_arr = map_to_array(file)

        if not validate_map_size(inputs_dict["map_size"]["width"], inputs_dict["map_size"]["height"], map_arr):
            print("map size not valid")
            continue

        if not validate_offices(map_arr, inputs_dict):
            print("offices not valid")
            continue

        print("file valid")