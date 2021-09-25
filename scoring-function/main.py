import os

outputs_path = "../outputs/"
inputs_path = "../validator/inputs/"

# This defines the movement function
movement = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

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

customer_offices = []

map_size = {
    "width": 20,
    "height": 11
}

def map_to_array(file):
    map_arr = []
    with open(inputs_path + file, "r") as f:
        # map starts at this part
        lines = f.readlines()[8:]
        for line in lines:
            # remove the new line
            line = line[:len(line)-1]
            map_arr.append(list(line))

    return map_arr

# reading output file and separating coordinates/paths
def paths_to_array(file):
    paths = []

    with open(outputs_path + file, "r") as f:
        # map starts at this part
        lines = f.readlines()
        for line in lines:
            parameters = line.split()
            # remove the new line

            path_array = []
            for path in parameters[2]:
                # remove the new line
                path_array.append(path)

            path_dict = {
                "x": int(parameters[0]),
                "y": int(parameters[1]),
                "path": path_array
            }

            paths.append(path_dict)

    return paths

# Finding the cost for the path
def path_cost(map, path):
    # Initial coordinate
    coordinate = [path["x"], path["y"]]
    cost = 0  # first movement doesn't count for the cost
    print(coordinate)

    # moving through the map
    for move in path["path"]:
        # calculating new coordinate
        coordinate = [coordinate[0] + movement.get(move)[0], coordinate[1] + movement.get(move)[1]]
        print(move)
        print(coordinate)

        # Checking if path is out of the map, if so, this path is incorrect and scores 0
        if coordinate[0] < 0 or coordinate[1] < 0:
            return 0
        elif coordinate[0] > map_size["height"] or coordinate[1] > map_size["width"]:
            return 0

        # checking what the terrain is in this coordinate
        terrain = map[coordinate[0]][coordinate[1]]

        # increasing cost of this path
        cost += terrain_cost.get(terrain)

    score = 0
    for customer_office in customer_offices:
        if coordinate in customer_office["coordinate"]:
            score = customer_office["reward"] - cost
            customer_office["reached"] = True

    if score < 0:
        return 0
    else:
        return score


def calculate_bonus():
    total_bonus = 0
    for customer_office in customer_offices:
        if not customer_office["reached"]:
            return 0

        total_bonus += customer_office["reward"]

    return total_bonus


if __name__ == "__main__":
    # reading in inputs
    input_files = os.listdir(inputs_path)
    # print(input_files)
    for file in input_files:
        map = map_to_array(file)  # same function as in validator
        print(map_to_array(file))

        # reading in outputs
        output_files = os.listdir(outputs_path)
        # print(output_files)
        for out_file in output_files:
            path_array = paths_to_array(out_file)

            score = 0
            for path in path_array:
                score += path_cost(map, path)

            score += calculate_bonus()







