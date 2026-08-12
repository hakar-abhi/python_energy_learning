def write_energy_data():
    f = open("energy_data.txt","w")
    f.write("Wind: 120\nSolar: 80\nHydro: 95")
    f.close()

# write_energy_data()
def read_energy_data():
    f = open("energy_data.txt","r")
    content = f.read()
    f.close()
    return content
# print(read_energy_data())

def read_energy_data_edit():
    with (open("energy_data.txt","r")) as f:
        return f.read()
# print(read_energy_data_edit())

def append_energy_data():
    with open("energy_data.txt","a") as f:
        f.write("\nBiomass: 60")
# append_energy_data()

def read_l_by_l():
    with open("energy_data.txt","r") as f:
        for reading in f:
            print(reading.strip())
# read_l_by_l()

def get_energy_lines():
    energy_data = []
    with open("energy_data.txt","r") as f:
        for lines in f:
            energy_data.append(lines.strip())
    return energy_data

# print(get_energy_lines())

def get_energy_dictionary():
    energy_dictionary = {}
    with open("energy_data.txt","r") as f:
        for line in f:
            line = line.strip()
            line = line.split(":")
            energy_dictionary[line[0]] = int(line[1])
    return energy_dictionary
# print(get_energy_dictionary())

def valid_energy_data():
    energy_data_dictionary ={}
    with open("energy_data.txt","r") as f:
        for part in f:
            part = part.strip()
            part_list =part.split(":")
            try:
                energy_data_dictionary[part_list[0]] = int(part_list[1])
            except (IndexError,ValueError):
                print(f"The errorneous line is {part}")
                
    return energy_data_dictionary
# print(valid_energy_data())

def safe_read_energy_file(filename):
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
# print(safe_read_energy_file("energy_data.txt"))
# print(safe_read_energy_file("missing_file.txt"))

def save_energy_dictionary(data, filename):
    with open(filename,"w") as f:
        for  key, value in data.items():
            f.write(f"{key}: {value}\n")
data = {
    "Wind": 120,
    "Solar": 80,
    "Hydro": 95
}

save_energy_dictionary(data, "saved_energy.txt")