import pandas as pd
import numpy as np


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
# print(new_data_frame)
get_wed_power = new_data_frame.loc["Wed","Power_MW"]
# print(get_wed_power)

get_data_tue_through_thu = new_data_frame.loc["Tue":"Thu"]
# print(get_tue_through_thu)
# print(type(get_tue_through_thu))

get_power_tue_through_thu = new_data_frame.loc["Tue":"Thu",["Power_MW"]]
# print(get_power_tue_through_thu)

get_power_tue_and_thu = new_data_frame.loc[["Tue","Thu"],["Power_MW"]]
# print(get_power_tue_and_thu)

get_wind_tue_and_thu = new_data_frame.loc[["Tue","Thu"],["Wind_m_s"]]
# print(get_wind_tue_and_thu)

subset_where_power_greater_120 = new_data_frame[new_data_frame["Power_MW"]>120]
# print(subset_where_power_greater_120)


mask_used = (new_data_frame["Power_MW"] >120) & (new_data_frame["Wind_m_s"]>6.5)
filtered_subset = new_data_frame[mask_used]
# print(filtered_subset)

new_mask = (new_data_frame["Power_MW"]>140) | (new_data_frame["Wind_m_s"]<6)
filtered_newsubset = new_data_frame[new_mask]
# print(filtered_newsubset)

sorted_power_descend = new_data_frame.sort_values(by="Power_MW",ascending=False)
# print(sorted_power_descend)

sorted_wind_ascend = new_data_frame.sort_values(by="Wind_m_s")
# print(sorted_wind_ascend)

sort_power_ascend_wind_descend = new_data_frame.sort_values(by=["Power_MW","Wind_m_s"],ascending=[True,False])
# print(sort_power_ascend_wind_descend)

sort_by_row_index = new_data_frame.sort_index(axis=0)
# print(sort_by_row_index)

sort_by_col_index = new_data_frame.sort_index(axis=1)
# print(sort_by_col_index)

##                 Dataframe Inspection / Healthcheck              ##

# print(new_data_frame.head())

# new_data_frame.info()
# print(new_data_frame.describe())

# print(new_data_frame.tail(2))

##                     Adding a new column         ##

new_data_frame["Power_kW"] = new_data_frame["Power_MW"]*1000
# print(new_data_frame)

new_data_frame["High_Power"] = new_data_frame["Power_MW"] > 130
# print(new_data_frame)

new_data_frame["Power_Category"] = np.where(new_data_frame["Power_MW"]>130,"High","Low")
# print(new_data_frame)

##                           Removing selected column and row            ##

modified_df = new_data_frame.drop(columns = ["Power_kW"])
# print(modified_df)

no_thu_df = new_data_frame.drop(index=["Thu"])
# print(no_thu_df)

no_thu_no_high_power = new_data_frame.drop(columns=["High_Power"],index=["Thu"])
# print(no_thu_no_high_power)

##             Renaming the columns, rows and index  ##

column_name_changed = new_data_frame.rename(columns={"Wind_m_s":"Wind_Speed_m_s"})
# print(column_name_changed)

row_name_changed = new_data_frame.rename(index={"Mon":"Monday"})
# print(row_name_changed)

rows_names_changed = new_data_frame.rename(index ={"Tue":"Tuesday","Wed":"Wednesday"})
# print(rows_names_changed)

index_name_changed = new_data_frame.copy()
index_name_changed.index.name = "Weekday"
# print(index_name_changed)

##                      Resetting the default index 0 1 2 3                 ##

original_index_df =new_data_frame.reset_index()
# print(original_index_df)

original_index_df_ohne_Day = new_data_frame.reset_index(drop=True)
# print(original_index_df_ohne_Day)

original_index_df = original_index_df.set_index("Power_MW")
# print(original_index_df)


# print(new_data_frame.describe())
# print(new_data_frame.describe(include="all"))

##                    Count the unique values                 ##

power_category = new_data_frame["Power_Category"]
count = power_category.value_counts()
# print(count)

unique_categories = power_category.unique()
# print(unique_categories)
# print(power_category.nunique())

##                           check if missing values exist          ##

check_na = power_category.isna()
print(check_na)









