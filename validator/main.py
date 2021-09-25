import os

path = "inputs/"

# TODO
# add constraints and other checks
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


if __name__ == "__main__":
    all_files = os.listdir(path)
    for file in all_files:
        # print(map_to_array(file))
        print(inputs_to_dict(file))

