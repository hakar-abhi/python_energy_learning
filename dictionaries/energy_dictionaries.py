def average_energy_use(energy_data):

    if not energy_data:
        return None
    total = 0
    for energy in energy_data.values():
        total+=energy
    result = total/len(energy_data)
    return result
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# avg_energy_usage = average_energy_use(energy_data)
# print("The average energy usage is: ",avg_energy_usage)

def highest_energy_data(energy_data):
    if not energy_data:
        return None
    highest = None
    for day, energy in energy_data.items():
        if highest is None or energy > highest:
            highest = energy
            highest_day = day
    return highest, highest_day
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = highest_energy_data(energy_data)
# highest,highest_day = result
# print("The highest energy consumption is: ", highest, "on", highest_day)

def day_above_average(energy_data):
    if not energy_data:
        return None
    total = 0
    new_list =[]
    for energy in energy_data.values():
        total+=energy
    average = total/len(energy_data)
    for day, energy in energy_data.items():
        if energy > average:
            new_list.append(day)
    return new_list

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = day_above_average(energy_data)
# print("The days above average energy use are: ", result)

def scale_energy_data(energy_data,factor):
    if not energy_data:
        return None
    new_dict ={}
    for day, energy in energy_data.items():
        scaled_energy = energy*factor
        new_dict[day] = scaled_energy
    return new_dict
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
factor = 1.1
# result = scale_energy_data(energy_data,factor)

# print("New sclaed energy data is: ", result)



def categorize_energy_use(energy_data):
    if not energy_data:
        return None
    new_dict = {}
    
    for day, energy in energy_data.items():
        if energy < 130:
            new_dict[day] = "Low"
            
        elif energy <=145:
            new_dict[day] = "Medium"

        else:
            new_dict[day] = "High"
    return new_dict

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = categorize_energy_use(energy_data)
# print(result)
        
def merge_dictionaries(data_a, data_b):

    if not data_a and not data_b:
        return None
    merged_dict = {}
    for day_a, energy_a in data_a.items():
        merged_dict[day_a] = energy_a
    for day_b, energy_b in data_b.items():
        if day_b in merged_dict:
            merged_dict[day_b]+=energy_b
        else:
            merged_dict[day_b] = energy_b

    return merged_dict
data_a = {"Monday": 100, "Tuesday": 120}
data_b = {"Tuesday": 30, "Wednesday": 140}

# result = merge_dictionaries(data_a,data_b)
# print(result)
        
def find_missing_days(energy_data, expected_days):
    list_of_missing_days =[]
    for day in expected_days:
        if day not in energy_data:
            list_of_missing_days.append(day)
    return list_of_missing_days

energy_data = {
    "Monday": 100,
    "Wednesday": 130,
    "Friday": 150
}
expected_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

# result = find_missing_days(energy_data,expected_days)
# print(result)

def fill_missing_days(energy_data, expected_days):

    new_energy_data = {}
    for day in expected_days:
        if day not in energy_data:
            new_energy_data[day] = 0
        else:
            new_energy_data[day] = energy_data[day]
    return new_energy_data
energy_data = {
    "Monday": 100,
    "Wednesday": 130,
    "Friday": 150
}
expected_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
# result = fill_missing_days(energy_data, expected_days)
# print(result)

def remove_invalid_readings(energy_data):
    new_energy_data = {}

    for day, energy in energy_data.items():
        if energy < 0:
            continue
        
        new_energy_data[day] = energy_data[day]
    return new_energy_data
energy_data = {
    "Monday": 100,
    "Tuesday": -20,
    "Wednesday": 0,
    "Thursday": 140
}
# result = remove_invalid_readings(energy_data)
# print(result)

def group_days_by_category(energy_data):

    new_data = {"Low": [],
                "Medium":[],
                "High":[]
                }


    for day, energy in energy_data.items():
        if energy < 130:
            new_data["Low"].append(day)
        elif energy <= 145:
            new_data["Medium"].append(day)
            
        else:
            new_data["High"].append(day)

    
    return new_data
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# result = group_days_by_category(energy_data)
# print(result)

def count_energy_category(energy_data):

    low_count = 0
    medium_count = 0
    high_count = 0

    new_data = {"Low": low_count,
                "Medium": medium_count,
                "High": high_count
                }
    for energy in energy_data.values():
        if energy < 130:
            new_data["Low"]+=1
        elif energy <=145:
            new_data["Medium"]+=1
        else:
            new_data["High"]+=1
    return new_data
energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}
# result = count_energy_category(energy_data)
# print(result)

def energy_range(energy_data):
    highest = None
    lowest = None
    if not energy_data:
        return None
    for energy in energy_data.values():
        if highest is None or energy > highest:
            highest = energy
        if lowest is None or energy < lowest:
            lowest = energy
    return highest,lowest

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = energy_range(energy_data)
# highest, lowest = result
# print("The range in energy consumption is highest: ",highest,"to lowest: ",lowest)

def energy_range(energy_data):
    highest = None
    lowest = None
    if not energy_data:
        return None
    for energy in energy_data.values():
        if highest is None or energy > highest:
            highest = energy
        if lowest is None or energy < lowest:
            lowest = energy
    return highest,lowest

energy_data = {
    "Monday": 120,
    "Tuesday": 135,
    "Wednesday": 128,
    "Thursday": 142,
    "Friday": 150
}

# result = energy_range(energy_data)
# highest, lowest = result
# print("The range in energy consumption is:",highest - lowest)

def peak_demand_summary(energy_data, threshold):
    if not energy_data:
        return None
    peak_days = []
    total = 0

    for day, energy in energy_data.items():
        if energy > threshold:
            peak_days.append(day)
            total+=energy

    number_of_peak_days = len(peak_days)
    return peak_days, number_of_peak_days, total

energy_data = {
    "Monday": 120,
    "Tuesday": 155,
    "Wednesday": 128,
    "Thursday": 170,
    "Friday": 150
}

threshold = 145

# result = peak_demand_summary(energy_data, threshold)
# peak_days, number_of_peak_days, total = result
# print("The peak days are:", peak_days)
# print("The number of peak days are:", number_of_peak_days)
# print("The total peak energy consumption is:",total)
    
def invert_energy_data(energy_data):

    new_data ={}

    for day, energy in energy_data.items():
        new_data[energy] = day
    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 155,
    "Wednesday": 128,
    "Thursday": 170,
    "Friday": 150
}

# result = invert_energy_data(energy_data)
# print(result)

def invert_energy_data(energy_data):
    new_data= {}

    for day, energy in energy_data.items():
        if energy in new_data:
            new_data[energy].append(day)

            
        else:
            new_data[energy] = [day]

    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120
}

# result = invert_energy_data(energy_data)
# print(result)


def count_energy_values(energy_data):
    new_data = {}
    
    for energy in energy_data.values():
        
        if energy in new_data:
            new_data[energy] +=1
        else:
            new_data[energy] = 1
          
    return new_data

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120,
    "Thursday": 150,
    "Friday": 130
}
# result = count_energy_values(energy_data)
# print(result)
        
def most_common_energy_value(energy_data):

    if not energy_data:
        return None
    new_data = {}
    largest = None
    for energy in energy_data.values():
        if energy in new_data:
            new_data[energy]+=1
        else:
            new_data[energy]=1
    
    for energy, count in new_data.items():
        if largest is None or count > largest:
            largest = count
            max_energy = energy
    return largest, max_energy

energy_data = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 120,
    "Thursday": 150,
    "Friday": 120
}

# result = most_common_energy_value(energy_data)

# largest, max_energy = result
# print(max_energy,",",largest)