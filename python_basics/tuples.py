##                   Tuples              ##

def summary_energy_values(values):
    if not values:
        return None
    swapped = True
    total = 0
    while swapped:
        position = 0
        swapped = False
        while position<(len(values)-1):

            if values[position]>values[position+1]:
                values[position+1],values[position]=values[position],values[position+1]
                swapped = True
            position+=1
    for value in values:
        total+=value
    
    smallest = values[0]
    largest = values[-1]
    average = total/len(values)
    result = (smallest,largest,average)
    return result
        
values = [120, 150, 130, 170, 140]
# result = summary_energy_values(values)
# print(result)

def energy_quality_summary(values):
    if not values:
        return None
    valid_count = 0
    invalid_count = 0
    zero_count = 0
    for value in values:
        if value > 0:
            valid_count+=1
        elif value == 0:
            zero_count+=1
        else:
            invalid_count+=1
    return (valid_count,zero_count,invalid_count)

values = [120, 0, 135, -5, 150, 0]
# result = energy_quality_summary(values)
# print(result)