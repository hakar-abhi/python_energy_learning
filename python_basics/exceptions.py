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
use_resource("30")
use_resource("bad")