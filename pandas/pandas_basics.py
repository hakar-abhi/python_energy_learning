import pandas as pd


##                      Creating a Series with default index    ##

data = [120, 135, 150, 110]

series_of_data = pd.Series(data)

# print(type(series_of_data))

# print(series_of_data)
# print(isinstance(series_of_data,pd.Series))

##                   Creating a series with custom index    ##

list_of_index = ["Mon", "Tue", "Wed", "Thu"]

series_w_custom_index = pd.Series(data,index=list_of_index)
# print(series_w_custom_index)

data_for_Wed = series_w_custom_index["Wed"]
# print(data_for_Wed)

data_for_Tue, data_for_Thu = series_w_custom_index[["Tue","Thu"]]
# print(data_for_Tue,data_for_Thu)

new_Tue_Thu_series = series_w_custom_index[["Tue","Thu"]]
# print(new_Tue_Thu_series)
# print(type(new_Tue_Thu_series))

##                             Use of .iloc()                       ##

get_wed = series_w_custom_index.iloc[2]
# print(get_wed)

##                            Use of .loc()                ##

tue_data,thu_data = series_w_custom_index.loc[["Tue","Thu"]]
# print(tue_data,thu_data)

data_from_1_3 = series_w_custom_index.iloc[1:4]
# print(data_from_1_3)

data_from_Tue_Thu = series_w_custom_index.loc["Tue":"Thu"]
# print(data_from_Tue_Thu)


##                 Boolean Filtering on Series  ##

series_greater_than_125 = series_w_custom_index[series_w_custom_index>125]
# print(series_greater_than_125)


mask = (series_w_custom_index>120) & (series_w_custom_index<150)
series_greater_120_less_150 = series_w_custom_index[mask]
# print(series_greater_120_less_150)

at_least_120 = series_w_custom_index[series_w_custom_index>=120]
# print(at_least_120)

get_index_labels = at_least_120.index
# print(get_index_labels)
# print(type(get_index_labels))

# print(series_w_custom_index)

# print(type(series_w_custom_index.index))
# print(type(series_w_custom_index.shape))
# print(type(series_w_custom_index.values))
# print(type(series_w_custom_index.dtype))
# print(type(series_w_custom_index.size))


##                                        Pandas Dataframe                     ##

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu"],
    "Power_MW": [120, 135, 150, 110],
    "Wind_m_s": [6.2, 7.1, 8.0, 5.8]
}

data_frame = pd.DataFrame(data)
# print(data_frame)
# print(type(data_frame))
# print(data_frame.dtypes)

only_power = data_frame["Power_MW"]
# print(only_power)

# print(data_frame.columns)
# print(data_frame.index)

custom_dataframe = data_frame[["Day","Power_MW"]]
# print(type(custom_dataframe))

row_at_2 = data_frame.iloc[2]
# print(type(row_at_2))

row_at_1_3 = data_frame.iloc[1:4]
# print(type(row_at_1_3))

value_at_row_2_col_1 = data_frame.iloc[2,1]
# print(value_at_row_2_col_1)

value_using_labels = data_frame.loc[2,"Power_MW"]


data_frame_copy = data_frame.copy()
new_data_frame = data_frame_copy.set_index("Day")
print(new_data_frame)
get_wed_power = new_data_frame.loc["Wed","Power_MW"]
print(get_wed_power)
