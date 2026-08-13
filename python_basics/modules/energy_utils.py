
def calculate_energy_efficiency(output,input_energy):
    return output/input_energy

def calculate_power_ratio(actual_power,rated_power):
    return actual_power/rated_power

if __name__ == "__main__":
    print(calculate_energy_efficiency(50,100))
