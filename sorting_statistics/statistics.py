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
# result = selection_sort(energy_values)
# print(result)


def finding_the_median(energy_values):
    if energy_values is None:
        return None

    size_of_list = len(selection_sort(energy_values))
    if size_of_list % 2 == 0:
        place = size_of_list//2
        median = (energy_values[place]+energy_values[place-1])/2
    else:
        place = size_of_list//2
        median = energy_values[place]
    return median
energy_values = [120, 180, 150, 130, 170, 140]
# result = finding_the_median(energy_values)
# print(result)

def summary(energy_values):
    if energy_values is None:
        return None
    sorted_values = selection_sort(energy_values)
    median_value = finding_the_median(sorted_values)
    total_range = sorted_values[len(sorted_values)-1]-sorted_values[0]
    total = 0
    for i in range(len(sorted_values)):
        total+=sorted_values[i]
    mean_value = total/len(sorted_values)
    return median_value, total_range, mean_value
# energy_values = [120, 150, 130, 170, 140]
# result = summary(energy_values)
# median_value, total_range, mean_value = result
# print("Median:",median_value,"Mean:",mean_value,"Range:",total_range)

def get_standard_deviation(energy_values):
    if not energy_values:
        return None
    result = summary(energy_values)
    median_value, total_range, mean_value = result
    total = 0
    for energy in energy_values:
        total+=(energy-mean_value)**2
    standard_deviation = (total/len(energy_values))**(0.5)
    return standard_deviation

energy_values = [120, 150, 130, 170, 140]
# result = get_standard_deviation(energy_values)
# print(result)

def get_zscore(energy_values):
    if not energy_values:
        return None
    total = 0
    for energy in energy_values:
        total+=energy
    mean_calc = total/len(energy_values)
    squared_total = 0
    for energy in energy_values:
        squared_total+=(energy-mean_calc)**2
    standard_deviation = (squared_total/len(energy_values))**0.5
    if standard_deviation==0:
        return None
    z_score_list=[]
    for energy in energy_values:
        z_score_list.append((energy-mean_calc)/standard_deviation)
    return z_score_list
energy_values = [120, 150, 130, 170, 140]
# result = get_zscore(energy_values)
# print(result)

def find_outliers(energy_values):
    if not energy_values:
        return None
    z_score_list = get_zscore(energy_values)
    if z_score_list is None:
        return None
    outlier_list = []
    for i in range(len(z_score_list)):
        if z_score_list[i]<-2 or z_score_list[i]>2:

            outlier_list.append(energy_values[i])

    return outlier_list,z_score_list
energy_values = [120, 125, 130, 128, 127, 190]

# result = find_outliers(energy_values)
# outliers,z_scores = result
# print("The list of outliers:",outliers)