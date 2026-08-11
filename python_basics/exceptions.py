values = [120, 0, 135, -5, 150, 0]
# result = energy_quality_summary(values)
# print(result)

##      exceptions handling with try/except      ##

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
# result = safe_divide(10,0)
# print(result)

def get_number():
    try:
        num = input("Enter a number: ")
        return float(num)
    except ValueError:
        return None
# result = get_number()
# print(result)

def get_list_item(values,index):
    try:
        return values[index]
    except IndexError:
        return None
# result = get_list_item([10, 20, 30], 5)
# print(result)

def get_dictionary_value(data,key):
    try:
        return data[key]
    except KeyError:
        return None

# print(get_dictionary_value({"wind": 120, "solar": 80}, "hydro"))

def read_number_from_list(values,index):
    try:
        number = float(values[index])
        return number
    except IndexError:
        
        return None
    except ValueError:
        return None
check_list = [(["10", "20.5", "abc"], 1),
              (["10", "20.5", "abc"], 5),
              (["10", "20.5", "abc"], 2)
              ]

# for values,index in check_list:
    
#     print(read_number_from_list(values,index))

def load_energy_value(data,key):
    try:
        return float(data[key])
    except KeyError:
        return None
    except ValueError:
        return None
    # print(load_energy_value({"wind": "120.5", "solar": "abc"}, "wind"))
    # print(load_energy_value({"wind": "120.5", "solar": "abc"}, "solar"))
    # print(load_energy_value({"wind": "120.5"}, "hydro"))

def divide_energy_values(data,key,divisor):
    try:
        return float(data[key])/divisor
    except (KeyError,ValueError,ZeroDivisionError):
        return None

data = {
    "wind": "120.5",
    "solar": "80",
    "hydro": "abc"
}
# print(divide_energy_values(data, "wind", 5))
# print(divide_energy_values(data, "solar", 4))
# print(divide_energy_values(data, "gas", 2))
# print(divide_energy_values(data, "wind", 0))
# print(divide_energy_values(data, "hydro", 2))

def parse_energy_value(value):
    try:
        value = float(value)
    except ValueError:
        return None
    else:
        return value*2
# print(parse_energy_value("12.5"))
# print(parse_energy_value("abc"))  

def process_energy_value(value):
    try:
        value = float(value)
    except ValueError:
        print("Invalid value")
    else:
        print(value)
    finally:
        print("Processing complete")
# process_energy_value("25.5")
# process_energy_value("abc")

def use_resource(values):
    try:
        print(float(values))
    except:
        print("Invalid value")
    finally:
        print("Resource closed")
# use_resource("30")
# use_resource("bad")

def validate_energy(value):
    if value<0:
        raise ValueError("Energy value can not be negative")
    return value

# print(validate_energy(50))
# print(validate_energy(-10))

def safe_validate_energy(value):
    try:
        return(validate_energy(value))
    except ValueError:
        return None
# print(safe_validate_energy(40))    
# print(safe_validate_energy(-5)) 

def report_energy_validation(value):
    try:
        return(validate_energy(value))
    except ValueError as error:
        print(error)
        return None
# print(report_energy_validation(25))
# print(report_energy_validation(-8))

def validate_wind_speed(value):
    if value < 0:
        raise ValueError("Wind speed can not be negative")
    if value > 100:
        raise ValueError("Wind speed is unrealistically high")
    return value
    
def safe_wind_speed(value):
    try:
        return(validate_wind_speed(value))
    except ValueError as error:
        print(error)
        return None
    return value
# print(safe_wind_speed(12))
# print(safe_wind_speed(-3))
# print(safe_wind_speed(150))
def validate_turbine_reading(reading):
    wind_speed = reading["wind_speed"]
    power = reading["power"]

    if reading["wind_speed"] < 0:
        raise ValueError("Invalid wind speed")
    if reading["power"] < 0:
        raise ValueError("Invalid power")
    return reading

# print(validate_turbine_reading({"wind_speed": 12, "power": 850}))
# print(validate_turbine_reading({"wind_speed": -2, "power": 850}))
# print(validate_turbine_reading({"wind_speed": 12, "power": -50}))

def safe_turbine_reading(reading):
    try:
        return validate_turbine_reading(reading)
    except (KeyError, ValueError) as error:
        print(f"Missing key: {error}")
        return None

# print(safe_turbine_reading({"wind_speed": 12, "power": 850}))
# print(safe_turbine_reading({"wind_speed": -2, "power": 850}))
# print(safe_turbine_reading({"wind_speed": 12, "power": -50}))
# print(safe_turbine_reading({"wind_speed": 12}))

def turbine_status(name,power,wind_speed):
    return f"Turbine {name} is producing {power} kW at {wind_speed} m/s"
# print(turbine_status("T1", 850, 12))

def calculate_capacity_factor(actual_energy, max_possible_energy):
    if max_possible_energy <=0:
        raise ValueError("Max possible energy must be positive")
    return actual_energy/max_possible_energy
# print(calculate_capacity_factor(500, 1000))
# print(calculate_capacity_factor(500, 0))

def safe_capacity_factor(actual_energy, max_possible_energy):
    try:
        return calculate_capacity_factor(actual_energy,max_possible_energy)
    except ValueError as error:
        print(error)
        return None

# print(safe_capacity_factor(500, 0))  

def calculate_power_ratio(actual_power,rated_power):
    try:
        actual_power = float(actual_power)
        rated_power =float(rated_power)
        if rated_power <= 0:
            raise ValueError("Rated power must be positive")
        return actual_power/rated_power
    except ValueError:
        return None
# print(calculate_power_ratio("500", "1000"))  
# print(calculate_power_ratio("abc", "1000"))   
# print(calculate_power_ratio("500", "0"))  

def process_turbine_power(data, key, rated_power):
    try:
        actual_power = float(data[key])
        rated_power =float(rated_power)
        if rated_power <= 0:
            raise ValueError("Rated power must be positive")
    except (KeyError,ValueError) as error:
        print(error)
        return None
    else:
        return actual_power/rated_power
    finally:
        print("Process is finished")
data = {
    "T1": "500",
    "T2": "abc"
}

print(process_turbine_power(data, "T1", "1000"))
print(process_turbine_power(data, "T2", "1000"))
print(process_turbine_power(data, "T3", "1000"))
print(process_turbine_power(data, "T1", "0"))