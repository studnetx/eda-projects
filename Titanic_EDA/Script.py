import numpy as np  # Numerical computing ka baap
import pandas as pd  # Data manipulation ki maa
import matplotlib.pyplot as plt  # Basic plotting ka dada
import seaborn as sns  # Beautiful plots ka chacha
import warnings
warnings.filterwarnings('ignore')  
# Choti moti warnings ko ignore 

df=pd.read_csv("/kaggle/input/datasets/stuentx/titanic-data-set/train.csv")
print('='*79)
print("Overview Of Data_Set")
print('='*79)
print(f"Shape Of Data_set :{df.shape}")
print(f"Rows in data_set :{df.shape[0]}")
print(f"Columns in data_set:{df.shape[1]}")
print(f"Name Of Columns :{df.columns}")

print('='*79)
print("Data Assessing")
print('='*79)
# basic state
print("basic state: ")
print(df.describe().T)
# missing values
print("missing values: ")
print(df.isna().sum())
# Duplicates
print("Duplicates: ")
print(df.duplicated().sum())
print("Info:")
print(df.info())

