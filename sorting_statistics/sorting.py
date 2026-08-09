def rank_based_sort_experiment(energy_values):
    sorted_energy_values = [0]*len(energy_values)

    for position in range(len(energy_values)):
        count = 0
        i = 0
        check = energy_values[position]
        if check in sorted_energy_values:
            dup_posn = sorted_energy_values.index(check)
            dup_posn+=1
            sorted_energy_values[dup_posn] = check
        else:

            while i < len(energy_values):
                    
                if check > energy_values[i]:
                    count+=1

                else:
                    count = count
                i+=1
            
                
            sorted_energy_values[count] = energy_values[position]
    return sorted_energy_values
energy_values = [120, 150, 130, 170, 140]
# result = rank_based_sort_experiment(energy_values)
# print(result)    

def bubble_sort(energy_values):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(energy_values)-1):
            
            if energy_values[i]>energy_values[i+1]:
                swapped = True
                energy_values[i], energy_values[i+1]=energy_values[i+1],energy_values[i]
        
    return energy_values

energy_values = [120, 150, 130, 170, 140]
# result = bubble_sort(energy_values)
# print(result)

def bubble_sort_descending(energy_values):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(energy_values)-1):
            
            if energy_values[i]<energy_values[i+1]:
                swapped = True
                energy_values[i], energy_values[i+1]=energy_values[i+1],energy_values[i]
        
    return energy_values

energy_values = [120, 150, 130, 170, 140]

# result = bubble_sort_descending(energy_values)
# print(result)

def selection_sort(energy_values):
    if not energy_values:
        return None
    position = 0
    
    while position < len(energy_values):
        smallest_index = position
        for i in range(position+1, len(energy_values)):
            if energy_values[i]<energy_values[smallest_index]:
                
                smallest_index = i
        energy_values[position],energy_values[smallest_index]=energy_values[smallest_index],energy_values[position]
        
        
        position+=1
    return energy_values

energy_values = [120, 180, 150, 130, 170, 140]
result = selection_sort(energy_values)
print(result)