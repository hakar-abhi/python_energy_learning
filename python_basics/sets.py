def unique_energy_values(values):
    unique_values = set()
    if not values:
        return unique_values
    for value in values:
        unique_values.add(value)
    return unique_values
values = [120, 150, 120, 130, 150]
# result = unique_energy_values(values)
# print(result)

def common_energy_values(values_a,values_b):
    if not values_a or not values_b:
        return set()
    values_a = set(values_a)
    values_b = set(values_b)
    common = values_a.intersection(values_b)
    return common
values_a = [120, 130, 150, 170]
values_b = [110, 130, 150, 180]
# result = common_energy_values(values_a,values_b)
# print(result)
    
def different_energy_values(values_a,values_b):

    values_a = set(values_a)
    values_b = set(values_b)
    different = values_a.symmetric_difference(values_b)
    return different
values_a = [120, 130, 150, 170]
values_b = [110, 130, 150, 180]
# result = different_energy_values(values_a,values_b)
# print(result)

def energy_only_in_a(values_a,values_b):
    values_a = set(values_a)
    values_b = set(values_b)
    return values_a.difference(values_b)

values_a = [120, 130, 150, 170]
values_b = [110, 130, 150, 180]
# result = energy_only_in_a(values_a,values_b)
# print(result)

def is_energy_subset(values_a,values_b):
    values_a = set(values_a)
    values_b = set(values_b)
    result = values_a.issubset(values_b)
    return result
values_a = [120, 130]
values_b = [110, 120, 130, 150]
# is_subset = is_energy_subset(values_a,values_b)
# print(is_subset)

def all_unique_energy_values(values_a,values_b):
    values_a = set(values_a)
    values_b = set(values_b)
    return values_a.union(values_b)
values_a = [120, 130, 150]
values_b = [130, 170, 180]
# result = all_unique_energy_values(values_a,values_b)
# print(result)

def are_disjoint(values_a,values_b):
    values_a = set(values_a)
    values_b = set(values_b)
    return values_a.isdisjoint(values_b)
values_a = [120, 130]
values_b = [150, 170]

# result = are_disjoint(values_a,values_b)
# print(result)   