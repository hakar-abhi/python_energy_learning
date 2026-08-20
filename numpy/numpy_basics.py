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
# print(equal_parts2)

split_with_indices = np.split(arr,[2,5])
# print(split_with_indices)

matrix3 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

split_in_h= np.hsplit(matrix3,2)
# print(split_in_h)


matrix4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

left, right = np.hsplit(matrix4,2)
# print(left,right)
joined = np.concatenate((left,right),axis=1)

# print(joined)
# print(joined.shape)

matrix5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print(matrix5.T.T)

a = np.array([10, 20, 30])
a_reshaped = np.reshape(a,(3,1))
# print(a_reshaped)
b= a.T 
# print(b)
power5 = np.array([100, 120, 100, 150, 120, 100, 170])
unique_power, counts = np.unique(power5, return_counts=True)
# print(unique_power)
# print(counts)

max_repeat_power = unique_power[np.argmax(counts)]
# print(max_repeat_power)

##   Array creation helpers ##

# Five zeros
five_zeros = np.zeros(5,).astype(int)
# print(five_zeros)

# Five ones
five_ones = np.ones(5,).astype(int)
# print(five_ones)

# Integers from 0 to 9

integers = np.arange(0,9)
# print(integers)

#Equal spaced values
equal_spaced_values = np.linspace(0,100,5).astype(int)
# print(equal_spaced_values)

# arange() with step
# print(np.arange(0,1,0.2))

# matrix of size (2,3) with all zeros
matrix_zeros = np.zeros((2,3))
# print(matrix_zeros)

# matrix of shape (3,2) all filled with 7
matrix_seven = np.full((3,2),7,dtype=int)
# print(matrix_seven)

# Identity matrix

I_matrix = np.eye(4,dtype=np.int64)
# print(I_matrix)
# print(I_matrix.shape)
# print(I_matrix.dtype)

# 1D array of 5 random integers from 1 to 10

random_1_10 = np.random.randint(1,10,5)
# print(random_1_10)

random_matrix = np.random.randint(1,100,(2,3))
# print(random_matrix)

random_matrix_float = np.random.rand(2,3)
# print(random_matrix_float)

random_10_20 = np.random.rand(2,3)*10+10
# print(random_10_20)

# random 3,4 float matrix in range[-5,5)

random_minus5to5 = np.random.rand(3,4)*10-5 
# print(random_minus5to5)

# matrix of random values from normal distribution with mean and sigma specified ir standard then 0 and 1
random_normal = np.random.standard_normal((2,3))
# print(random_normal)

# generate 10,000 random normal values and find mean and standard deviation
random_standard_normal_10000 = np.random.standard_normal(10000)
# print(random_normal_10000.mean())
# print(random_normal_10000.std())

random_normal_50_10 = np.random.normal(50,10,10000)
# print(random_normal_50_10.mean())

# use of np.random.seed(42)

# np.random.seed(42)
# print(np.random.randint(1,100,5))

# np.random.seed(41)
# print(np.random.randint(1,100,5))

# np.random.seed(42)

a = np.random.randint(1, 100, 5)
b = np.random.randint(1, 100, 5)

# print(a)
# print(b)


# dtype conversion and memory 

values = np.array([10, 20, 30, 40, 50]).astype(np.float32)
# print(values.dtype)
# print(values.itemsize)
# print(values.nbytes)

values1 = np.array([1.5, 2.7, 3.9], dtype=np.float32)
values1 = values1.astype(np.int32)
# print(values1)

#                  Missing values with np.nan           ##

data = np.array([10.0, 20.0, np.nan, 40.0, 50.0])
# print(np.isnan(data))
# print(data.mean())
mean_value_w_nan = np.nanmean(data)
max_value_w_nan = np.nanmax(data)
min_value_w_nan = np.nanmin(data)
total_w_nan = np.nansum(data)
# print(mean_value_w_nan, max_value_w_nan,min_value_w_nan,total_w_nan)


##                     Replacing missing values             ##

data = np.where(np.isnan(data),np.nanmean(data),data)
# print(data)

data1 = np.array([10.0, 20.0, np.nan, 40.0, 50.0])
logic = (np.isnan(data1)) | (np.isinf(data1))
logic_edit = ~np.isfinite(data1)
# print(logic_edit)
# print(logic)


data2 = np.array([10.0, np.nan, 25.0, np.inf, -np.inf, 40.0])
logic2 = (np.isnan(data2)) | (np.isinf(data2))
# data2 = np.where(logic2,0,data2)
data3 = np.where(np.isfinite(data2), data2, 0)
# print(data3)

total_inf_nans = np.sum(~np.isfinite(data2))
# print(total_inf_nans)

data4 = data2.copy()
data4 = np.where(np.isfinite(data2), data2, 0)

##              View mode vs copy mode              ##

original = np.array([10, 20, 30, 40, 50])

slice_view = original[1:4]
# print(slice_view)

slice_view[0] = 999
# print(slice_view.base)
# print(slice_view)
# print(original)

##                               Squeeze  and expand_dims method                 ##

arr = np.array([[[10], [20], [30]]])
# print(arr.shape)
# print(arr.ndim)

arr_copy = arr.copy()
arr_copy = np.squeeze(arr_copy)
# print(arr_copy.shape)

arr3 = np.array([10, 20, 30])

arr3_copy1 = arr3.copy()
arr3_copy2 = arr3.copy() 

arr3_copy1 = np.expand_dims(arr3_copy1,axis=0)
# print(arr3_copy1)

arr3_copy2 =np.expand_dims(arr3_copy2,axis=1)
# print(arr3_copy2)

arr3_copy3 = arr3.copy()
arr3_copy3 = np.expand_dims(arr3,axis=1)
arr3_copy4 = np.expand_dims(arr3_copy3,axis=0)
# print(arr3_copy4.shape)

arr_ = np.array([10,20,30])
arr_column = arr_[np.newaxis,:]
# print(arr_column.shape)
# print(arr_column)

arr_row = arr_[:,np.newaxis]
# print(arr_row)
# print(arr_row.shape)
# print(arr_)

matrix5 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

matrix5_selected_rows = matrix5[[0,2]]
# print(matrix5_selected_rows)

matrix_5_selected_columns = matrix5[:,[0,2]]
# print(matrix_5_selected_columns)

selected = matrix5[[0,2],[2,0]]

# print(selected)

##             Advanced Selection with np.ix_()              ##

rows = [0,2]
columns=[0,2]

sub_matrix = matrix5[np.ix_(rows,columns)]
# print(sub_matrix)


##          Selection with np.take(array,[indices])       ##
arr = np.array([10, 20, 30, 40, 50])
selection_w_fancy = arr[[0,2,4]]
selection_w_take = np.take(arr,[0,2,4])
# print(selection_w_fancy)
# print(selection_w_take)

select_rows = np.take(matrix5,[0,2],axis=0)
# print(select_rows)

select_columns = np.take(matrix5,[0,2],axis=1)
# print(select_columns)

select_custom = np.take(matrix5,[2,0,2],axis=1)
# print(select_custom)

seelct_col_1 = np.take(matrix5,[1],axis=1)
select_col_1_normal = matrix5[:,1]
# print(seelct_col_1.shape)
# print(select_col_1_normal.shape)


##                            Use of np.delete()             ##
arr = np.array([10, 20, 30, 40, 50])

new_arr = np.delete(arr,[1,3])
# print(new_arr)
# print(arr)

del_row_1 = np.delete(matrix5,1,axis=0)
# print(del_row_1)

##                          Use of np.insert()           ##

arr = np.array([10, 20, 30, 40])

new_arr = np.insert(arr,2,25)
# print(new_arr)
# print(arr)

matrix = np.array([
    [10, 20],
    [30, 40]
])

new_matrix = np.insert(matrix,1,[50,60],axis=0)
new_matrix_w_col = np.insert(matrix,1,[50,60],axis=1)
# print(new_matrix_w_col)

##                    Use of np.append()         ##

new_appended = np.append(matrix,[[50,60]],axis=0)
# print(new_appended)

new_appended_col = np.append(matrix,[[50],[60]],axis=1)
# print(new_appended_col)

##                    Use of np.repeat()         ##

arr = np.array([10, 20, 30])
new_arr_repeat=  np.repeat(arr,2)
# print(new_arr_repeat)

matrix = np.array([
    [1, 2],
    [3, 4]
])

new_matrix =np.repeat(matrix,2,axis=0)
# print(new_matrix)

matrix_new = np.repeat(matrix,[1,3],axis=0)
# print(matrix_new)

arr = np.array([10, 20, 30])
arr_new = np.repeat(arr,[1,2,3])
# print(arr_new)

##                              Use of np.tile()            ##
new_arr_tile = np.tile(arr,2)
# print(new_arr_tile)

new_arr_tile_rows = np.tile(arr,(3,1))
# print(new_arr_tile_rows)


##                   Use of np.flip()         ##

arr = np.array([10, 20, 30, 40])
reversed =np.flip(arr)
# print(reversed)
# print(arr)

new_array = arr[::-1]
# print(new_array)
# print(arr)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row_flipped = np.flip(matrix,axis=0)
col_flipped = np.flip(matrix,axis=1)
# print(row_flipped)
# print(col_flipped)


##    NumPy Sorting  ##

power = np.array([150, 90, 200, 120, 170])
sorted_indices = np.argsort(power)
# print(sorted_indices)
# print(power[sorted_indices])
# print(np.flip(sorted_indices))
power_sort_descend = np.flip(power[sorted_indices])
# print(power_sort_descend)

matrix = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

row_sort_ind = np.argsort(matrix,axis=0)
col_sort_ind = np.argsort(matrix,axis=1)
# print(row_sort_ind)
# print(col_sort_ind)

row_sort = np.sort(matrix,axis=0)
col_sort = np.sort(matrix,axis=1)

# print(row_sort)
# print(col_sort)

index_of_max_row_value = np.argmax(matrix,axis=1)
# print(index_of_max_row_value)


##                        Find max value with np.max()           ##
max_row_value = np.max(matrix, axis=1)
# print(max_row_value)

##                       2D Boolean Filtering plus axis              ##

matrix = np.array([
    [30, 10, 20],
    [60, 40, 50],
    [25, 70, 15]
])

count_greater_than30 = np.sum(matrix>30,axis=1)
# print(count_greater_than30)

##                      Replace values < =30 by NaN then find NaN safe mean       ##

matrix_replaced = np.where(matrix<=30,np.nan,matrix)
# mean_each_col = np.nanmean(matrix_replaced,axis=0)
# # print(mean_each_col)

# count_greaterthan_equal40 = np.sum(matrix>=40,axis=1)
# # print(count_greaterthan_equal40)

# percentage_greater_thanequal40 = (count_greaterthan_equal40/matrix.shape[1])*100
# print(percentage_greater_thanequal40)


##                            Linear Algebra                     ##

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a,b)
result_ = a@b
# print(result)
# print(result_)


A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# print(A@B)
# print(A*B)

# b = np.array([10, 20])
# print(A*b)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

# result_mul = A@B
# print(result_mul.shape)

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# C = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print(A@C)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 20, 30])

result_1D_2_3_matrix = A@v
# print(result_1D_2_3_matrix)
# print(result_1D_2_3_matrix.shape)

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

v = np.array([10, 20, 30])

# print((v@A).shape)

##             Transpose      ##
A_transpose = A.T
# print(A_transpose)

# print(A@A.T)
# print(A.T@A)

M = A@A.T
# print(np.array_equal(M,M.T))


##                 np.any() np.all()
values = np.array([10, 20, 30, 40, 50])

# print(np.any(values==30))
# print(np.all(values>60))

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.all(matrix,axis=1)>15)



