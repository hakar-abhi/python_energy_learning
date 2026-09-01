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
# print(check_na)

s = pd.Series([10, np.nan, 30, np.nan, 50])
# print(s)

total_missing_values = s.isna().sum()
# print(f"Total missing values: {total_missing_values}")

new_s = s[~s.isna()]
# print(new_s)

##                   Keeping only non missing values       ##

filtered_s = s.dropna()
# print(filtered_s)

s_with_index_reset = filtered_s.reset_index(drop=True)
# print(s_with_index_reset)

s_missing_filled_with_zero = s.fillna(0)
# print(s_missing_filled_with_zero)

s_missing_filled_w_mean = s.fillna(s.mean())
# print(s_missing_filled_w_mean)

s_fill_w_prev_valid_value = s.ffill()
# print(s_fill_w_prev_valid_value)

s_fill_w_next_valid_value = s.bfill()
# print(s_fill_w_next_valid_value)

test_s = pd.Series([np.nan, 4, "cristiano", "is", "gay", np.nan, 4, np.nan])
test_s_w_bfill_n_ffill = test_s.bfill().ffill()
test_s_w_ffill_n_bfill = test_s.ffill().bfill()

# print(test_s_w_bfill_n_ffill)
# print(test_s_w_ffill_n_bfill)

##           Identify Duplicates & keep only the unique ones          ##

s = pd.Series([10, 20, 20, 30, 40, 40, 40, 50])

# print(s.duplicated())

keep_non_duplicates = s.drop_duplicates()
# print(keep_non_duplicates)

keep_non_duplicates_last_occurence = s.drop_duplicates(keep="last")
# print(keep_non_duplicates_last_occurence)

##          Duplicates filtering in DataFrame         ##

df = pd.DataFrame({
    "Turbine": ["T1", "T1", "T2", "T2", "T2"],
    "Power_MW": [2.1, 2.1, 1.8, 1.9, 1.9]
})

# print(df.duplicated())

keep_first_remove_dups = df.drop_duplicates()
# print(keep_first_remove_dups)

turbine_duplicates_df = df.duplicated(subset=["Turbine"])
# print(turbine_duplicates_df)

df_ohne_duplicates_turbine = df.drop_duplicates(subset=["Turbine"])
# print(df_ohne_duplicates_turbine)

##                       Datatype identification & conversion                  ##


df = pd.DataFrame({
    "Power_MW": ["120", "135", "150", "110"],
    "Wind_m_s": [6.2, 7.1, 8.0, 5.8]
})

# print(df.dtypes)

df = df.astype({"Power_MW":"int64"})
# print(df.dtypes)

df = pd.DataFrame({
    "Power_MW": ["120", "135", "bad", "110"],
    "Wind_m_s": [6.2, 7.1, 8.0, 5.8]
})

# print(df.dtypes)

df["Power_MW"] = pd.to_numeric(df["Power_MW"],errors="coerce")
# print(df["Power_MW"])

# df = df.astype({"Power_MW":"int64"},errors="ignore")
# print(df)
# print(df.dtypes)

total_missing = df["Power_MW"].isna().sum()
# print(total_missing)

# print(df)

cleaned_df = df.dropna(subset=["Power_MW"])
# print(cleaned_df)

cleaned_df = cleaned_df.reset_index(drop=True)
# print(cleaned_df)

filled_df = df.copy()

filled_df["Power_MW"] = filled_df["Power_MW"].fillna(filled_df["Power_MW"].mean())
# print(filled_df)


data_provided = {
    "Location" : [np.nan, "Dortmund", "Berlin",np.nan],
    "Salary" : [np.nan, np.nan, 720000, 60000],
    "Category": ["TSO", "TSO","TSO", "TSO"]
}

df = pd.DataFrame(data = data_provided, index=["Tennet","Amprion","50Hertz","Transnet"])
# print(df)

cleaned_df_ = df.dropna()
# print(cleaned_df_)
# print(df.dtypes)
# print(df.shape)
# print(df.describe(include="all"))

only_salary_miss_df = df.dropna(subset=["Salary"])

salary_location_miss_df = df.dropna(
    subset=["Salary","Location"], 
    how="all"
    )
# print(salary_location_miss_df)

df["Location"] = df["Location"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# print(df)

# print(df.isna().any().any())


##                             String cleaning               ##

df = pd.DataFrame({
    "Turbine": [" T1", "T2 ", " T3 ", "T4","T5"],
    "Status": [" running", "STOPPED ", " Running ", "stopped","maintenance"]
})

# print(df)

df["Turbine"] = df["Turbine"].str.strip()
df["Status"] = df["Status"].str.strip().str.lower()

# print(df)

mask = (df["Status"] == "running")
# print(mask)

df.insert(2,"Status_Bool",mask)

df.insert(3,"Status_Code",(np.where(df["Status"]=="running",1,0)))

mapping = {
    "running":"Active",
    "stopped" : "Inactive"
}

df.insert(
    4,
    "Status_Label",
    df["Status"].map(mapping)
)

df = df.replace(["running","stopped"],["Active","Inactive"])


edited_df = df.copy()

new_df = df.copy()


mask = edited_df["Status"].str.contains("a")

edited_df = edited_df[mask]

# print(edited_df)

filtering_start = edited_df["Status"].str.startswith("A")
filtering_end = edited_df["Status"].str.endswith("e")

mask_used = filtering_start | filtering_end

# print(filtering_start)
# print(filtering_end)

starting_with_df = edited_df[filtering_start]
ending_with_df = edited_df[filtering_end]

filtered_df = edited_df[mask_used]

# print(filtered_df)

# mask_contains = (new_df["Status"].str.contains(("active"),case=False)) | (new_df["Status"].str.contains(("maint"),case=False))

# new_df = new_df[mask_contains]

# print(new_df)


##                            Filtering with regex          ##

mask_ = new_df["Status"].str.contains("active|maint",case=False)
new_df = new_df[mask_]
# print(new_df)

new_df["Status"] = new_df["Status"].str.replace("maint","service")
# print(new_df)

new_df.insert(5,"Status_Length",new_df["Status"].str.len())
new_df.insert(6,"Turbine_Number",new_df["Turbine"].str.extract(r"(\d+)"))

new_df["Turbine_Number"] = pd.to_numeric(new_df["Turbine_Number"],errors="coerce")

# print(new_df["Turbine_Number"].dtype)


# print(starting_with_df)
# print(ending_with_df)


df = pd.DataFrame({
    "Asset_ID": ["WT-101", "WT-205", "PV-310", "WT-412"]
})

# df.insert(1,"Asset_Type",df["Asset_ID"].str.extract(r"([A-Z]+)"))
df.insert(1,"Asset_Type",df["Asset_ID"].str.split("-").str[0])
df.insert(2,"Asset_Number",df["Asset_ID"].str.extract(r"(\d+)"))

df["Asset_Number"] = pd.to_numeric(df["Asset_Number"])



mask = (df["Asset_Type"] == "WT") & (df["Asset_Number"] > 200)

filtered_df = df[mask]

# print(df.head())

# print(filtered_df.head())

##                    Counting how many counts do each category have                ##

each_category = df["Asset_Type"].value_counts()

# print(each_category)


##              Grouping by category and finding mean of each category       ##

# # print(df.groupby("Asset_Type")["Asset_Number"].mean())
# print(df)
# print(df.groupby("Asset_Type")["Asset_Number"].mean())
# print(df.groupby("Asset_Type")["Asset_Number"].max())

# print(df.groupby("Asset_Type")["Asset_Number"].agg(["mean","max"]))

# print(df.groupby("Asset_Type")["Asset_Number"].agg(["count","mean","min","max"]))


df = pd.DataFrame({
    "Asset_Type": ["WT", "WT", "PV", "PV", "WT"],
    "Asset_Number": [101, 205, 310, 412, 250],
    "Power_MW": [2.1, 2.4, 1.2, 1.5, 2.3]
})

# group_1 = df.groupby("Asset_Type").agg({"Asset_Number":["mean","max"],
#                                         "Power_MW":["mean","min"]})
# print(group_1)

df = pd.DataFrame({
    "Asset_Type": ["WT", "WT", "PV", "PV", "WT"],
    "Site": ["North", "South", "North", "South", "North"],
    "Power_MW": [2.1, 2.4, 1.2, 1.5, 2.3]
})

group_2 = df.groupby(["Asset_Type","Site"])["Power_MW"].mean()

group_2 = group_2.reset_index()
# print(group_2)

group_3 = df.groupby("Site")["Power_MW"].agg(["min","max"])

group_3["range"] = group_3["max"]-group_3["min"]

# print(group_3)


##                          Named Aggregation                      ##

group_4 = df.groupby("Asset_Type").agg(Average_Power_MW = ("Power_MW","mean"))
print(group_4)

group_5 = df.groupby("Asset_Type").agg(Average_Power_MW = ("Power_MW","mean"),
                                       Maximum_Power_MW = ("Power_MW","max"),
                                       Asset_Count = ("Power_MW","count")


)

group_6 = df.groupby("Site").agg(
    Average_Power_MW = ("Power_MW","mean"),
    Minimum_Power_MW = ("Power_MW","min"),
    Maximum_Power_MW = ("Power_MW","max")

)

print(group_6)



















# print(df["Asset_Number"].dtype)






# print(df)























