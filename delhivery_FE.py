
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

hyptoythesis testing





