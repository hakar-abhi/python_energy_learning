def moving_average(values,window):
    if not values or window <= 0 or window > len(values):
        return None
    position = 0
    result = []
    
    while (position+window) <= len(values):
        total=0
        for i in range(position,position+window):
            total+=values[i]
        result.append(total/window)
        position+=1
    return result
values = [10, 20, 30, 40, 50]
window_size = 3
# moving_averaged_values = moving_average(values,window_size)
# print(moving_averaged_values)

def rolling_max(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    position = 0
    result = []
    while (position+window_size)<=len(values):
        largest=values[position]
        for i in range(position,position+window_size):
            if values[i]>largest:
                largest=values[i]
        result.append(largest)
        position+=1
    return result
# values = [10, 20, 30, 40, 50]
# window_size=3
# max_values = rolling_max(values,window_size)
# print(max_values)


def rolling_min(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    position = 0
    result = []
    while (position+window_size)<=len(values):
        smallest=values[position]
        for i in range(position,position+window_size):
            if values[i]<smallest:
                smallest=values[i]
        result.append(smallest)
        position+=1
    return result
values = [10, 20, 30, 40, 50]
window_size=3
# min_values = rolling_min(values,window_size)
# print(min_values)

def rolling_range(values,window_size):
    if not values or window_size <=0 or window_size > len(values):
        return None
    min_values = rolling_min(values,window_size)
    max_values = rolling_max(values,window_size)
    result = []
    for i in range(len(min_values)):
        result.append(max_values[i]-min_values[i])
    return result
values = [10, 20, 15, 30, 25]
window_size = 3
range_values = rolling_range(values,window_size)
print(range_values)