
## DELHIVERY DATA ANALYSIS
print("DELHIVERY DATA ANALYSIS")
=======
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from sklearn.impute import KNNImputer



df = pd.read_csv("/workspaces/SCLR_Delhivery_FE/delhivery_data.csv")
df.head()
df.shape
df.columns
df.info()

df["trip_creation_time"] = pd.to_datetime(df["trip_creation_time"])

df["od_start_time"] = pd.to_datetime(df["od_start_time"])
df["od_end_time"] = pd.to_datetime(df["od_end_time"])




df = df.isnull().sum()

df = df.dropna(how = "any")

groupy by order id, any( lambda x : x)) 

difference between osrm and actual delivery time. 

difference between actual delivery time and actual osrm time.

create dictionary for a dataframe creation with relevant information for a particular study

>> check the functions/string used for agg() function. use the strings first and last for specifying start and end of a check-point.

hyptoythesis testing

z score - finding and eliminating/capping outliers for normally distributed data. 

standardization and normalization of data. 

Create a dataframe with required columns for a particular study
  
check problem description on Scaler

update time error table. 

remove outliers and calculate the mean of the time error. 

plot a graph of means and see the kind of distribution. 

