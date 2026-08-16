import numpy as np

numbers = [120, 135, 150, 140, 160]
array = np.array(numbers)
# print(array)

# print(array.ndim)
# print(array.shape)
# print(array.size)

# print(type(array))

##                 Indexing and Slicing                  ##

data = [
    [120, 135, 150],
    [140, 160, 170]
]

data = np.array(data)
# print(data)
# print(data.ndim)
# print(data.shape)
# print(data.size)

array = np.array([
    [120, 135, 150],
    [140, 160, 170]
])

# print(array[1,1])
# print(array[0,:])
# print(array[:,1])
# print(array[0,1:])
# print(array[:,1:])
# print(array[:,:2])
# print(array[:,2])

##      Vectorized Operation           ##

array = np.array([120, 135, 150, 140, 160])
array_plus = array + 10
array_mult = array * 2
# print(array_plus)
# print(array_mult)

actual = np.array([120, 135, 150, 140, 160])
predicted = np.array([125, 130, 148, 145, 158])

error = predicted - actual
# print(error)
# print(error.dtype)

#           Using NumPy methods             #

array = np.array([120, 135, 150, 140, 160])
maximum_value = np.max(array)
minimum_value = np.min(array)
total = np.sum(array)
mean_value = np.mean(array)
range_value = maximum_value-minimum_value
# print(f"Max: {maximum_value}, Min: {minimum_value}, Total: {total}, Mean: {mean_value}, Range: {range_value}")

logic_and = (array>=135) & (array<160)
filtered_array  = array[logic_and]

#print(filtered_array)

logic_or = (array<130) | (array>150)
filtered_or = array[logic_or]
# print(filtered_or)

logic_not = array != 140
filtered_not = array[logic_not]
# print(filtered_not)

# print(np.sum(array>140))

power = np.array([80, 120, 150, 90, 170, 200, 110])

# print(np.mean(power[power>=150]))
# print(np.argmax(power))

# power_sort = np.sort(power)
# print(power_sort)
# print(power)


# power_sort_descend = power_sort[::-1]
# print(power_sort_descend)

# reshaped_array = power.reshape(2,3)
# reshaped_array_2 = power.reshape(3,2)
# print(reshaped_array)
# print(reshaped_array.shape)
# print(reshaped_array.ndim)

# print(reshaped_array_2)
# print(reshaped_array_2.shape)
# print(reshaped_array_2.ndim)

# check = power.reshape(2,-1)
# print(check.shape)
# print(check.size)
# print(check.ndim)

# check2 = power.reshape(-1,2)
# print(check2.shape)
# print(check2.size)
# print(check2.ndim)

matrix = np.array([
    [80, 120, 150],
    [90, 170, 200]
])
# print(matrix.shape)
# print(matrix.ndim)

# flattened = matrix.reshape(-1)
# print(flattened)
# print(flattened.shape)
# print(flattened.ndim)

# flattened_2 = matrix.ravel()
# print(flattened_2.ndim)
# print(flattened_2.shape)

# flattened_3 = matrix.flatten()
# print(flattened_3.ndim)
# print(flattened_3.shape)

# print(np.sum(matrix,axis=0))
# print(np.sum(matrix,axis=1))

# print(np.mean(matrix,axis=0))
# print(np.mean(matrix,axis=1))

# print(np.max(matrix, axis=0))
# print(np.argmax(matrix,axis=0))

# print(np.std(power))
# print(np.var(power))

# print(np.sqrt(np.var(power)) == np.std(power))  ##better use np.isclose()

# print(np.median(power))
# print(np.quantile(power,0.25))
# print(np.quantile(power,0.5))
q25 = np.quantile(power,0.25)
q75 = np.quantile(power,0.75)
filtered_power = power[power>=q75]
# print(filtered_power)

threshold = (power>=q25) & (power<=q75)
# print(power[threshold])

power_result = np.where(power<120,0,power)
more_than_150 = np.where(power>=150,1,0)
# print(more_than_150)
# print(power_result.shape)

power_btn_100_180 = np.clip(power,100,180)
# print(power_btn_100_180)

efficiency = np.array([0.8234, 0.9178, 0.7562, 0.8899])

# print(np.round(efficiency,2))
# print(np.round(efficiency*100,2))

values = np.array([4, 9, 16, 25, 36])

sqaure_root_value = np.sqrt(values)
squared_value = values ** 2
# print(sqaure_root_value)
# print(squared_value)
# # 
# print(np.log(values))
# print(np.log10(values))

energy = np.array([10, 20, 15, 25, 30])

cumulative_sum = np.cumsum(energy)
# print(cumulative_sum)

# print(np.cumprod(energy))

power2 = np.array([100, 120, 115, 140, 150])

jumps = np.diff(power2)
max_jump = np.max(jumps)
# print(jumps)
# print(np.argmax(jumps))

# print(np.min(jumps))

value_before_largest_jump = power2[np.argmax(jumps)]
# print(value_before_largest_jump)

value_after_largest_jump = power2[np.argmax(jumps)+1]
# print(value_after_largest_jump)
power3 = np.array([100, 120, 120, 110, 135])
changes = np.diff(power3)
# print(changes)
change_sign = np.sign(changes)
# print(change_sign)
total_increase = np.sum(change_sign==1)
# print(total_increase)
filtered_changes = changes[changes>0]
# print(np.mean(filtered_changes))

filtered_neg = changes[changes<0]
# print(np.mean(np.abs(filtered_neg)))

largest_change_index = np.argmax(np.abs(changes))
# print(largest_change_index)

largest_change_with_sign = changes[largest_change_index]
# print(largest_change_with_sign)

##                  Normalize an array to 0-1 range           ##

power4 = np.array([80, 120, 150, 90, 170, 200, 110])
# print((power4-np.min(power4))/(np.max(power4)-np.min(power4)))


##                            z score standardization          ##

z_score_values = (power4-np.mean(power4))/np.std(power4)
# print(z_score_values)

filtered_values = power4[z_score_values>1]
# print(filtered_values)

between = power4[(z_score_values>=-1) & (z_score_values<=1)]
# print(between)

# print(np.sum((z_score_values<-1) | (z_score_values>1)))

out_of_bound_values = power4[(z_score_values<-1)|(z_score_values>1)]
# print(out_of_bound_values)

get_index = np.where((z_score_values<-1)|(z_score_values>1))[0]
# print(get_index)

##           Boolean mask for matrices            ##

matrix2 = np.array([
    [80, 120, 150],
    [90, 170, 200]
])

values_greater_than_120 = matrix2[matrix2>120]
# print(values_greater_than_120)

filtered_matrix = np.where(matrix2<=120,0,matrix2)
# print(filtered_matrix)

##                      NumPy Broadcasting           ##

offsets = np.array([10,20,30])
# print(offsets.shape)

# result = matrix2+offsets
# print(result.shape)
# print(result)

row_offsets = np.array([
    [10],
    [20]
])
# print(row_offsets.shape)

result2 = matrix2+row_offsets
# print(result2)
# print(result2.shape)


##                     Stacking            ##

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

c = np.stack((a,b),axis=0)
# print(c.shape)
# print(c)
c_edit = np.vstack((a,b))
# print(np.array_equal(c,c_edit))

d = np.stack((a,b),axis=1)
# print(d)
# print(d.shape)

hstack = np.hstack((a,b))
# print(hstack)

##                  Concatenating           ##

concatenated = np.concatenate((a,b))
# print(concatenated)

a2 = np.array([
    [1, 2],
    [3, 4]
])

b2 = np.array([
    [5, 6],
    [7, 8]
])

a2b2 = np.concatenate((a2,b2), axis = 1)
# print(a2b2)

stack_work = np.stack((a2,b2),axis=0)
# print(stack_work)
# print(stack_work.shape)

arr = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([10, 20, 30, 40, 50, 60, 70])

# equal_parts = np.split(arr2,3)
# print(equal_parts)

equal_parts2 = np.array_split(arr2,3)
print(equal_parts2)






