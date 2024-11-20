
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
