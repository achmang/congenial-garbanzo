import os

outputs_path = "../outputs/"
inputs_path = "../inputs/"

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
                "x": parameters[0],
                "y": parameters[1],
                "path": path_array
            }

            paths.append(path_dict)

    return paths


if __name__ == "__main__":
    # reading in inputs
    # input_files = os.listdir(inputs_path)
    # print(input_files)
    # for file in input_files:
    #     print(map_to_array(file))

    # reading in outputs
    output_files = os.listdir(outputs_path)
    print(output_files)
    for file in output_files:
        print(paths_to_array(file))

