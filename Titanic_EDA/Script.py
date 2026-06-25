import numpy as np  # Numerical computing ka baap
import pandas as pd  # Data manipulation ki maa
import matplotlib.pyplot as plt  # Basic plotting ka dada
import seaborn as sns  # Beautiful plots ka chacha
import warnings
# Choti moti warnings ko ignore 
warnings.filterwarnings('ignore')  

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


def classify_variables(data):
    """Variables ko categorical aur numerical mein divide karna"""
    cat = []
    num = []
    for col in data.columns:
        if data[col].dtype == 'object':
            cat.append(col)
        elif data[col].dtype in ['int64', 'float64']:
            if data[col].nunique() < 10:  # Agar unique values kam hain toh treat as categorical
                cat.append(col)
            else:
                num.append(col)
    return cat, num


cat_vars, num_vars = classify_variables(df)
print("="*79)
print("🎨 Variable Classification:")
print("="*79)
print("Categorical_Features :\n",cat_vars)
print("Numerical_Features :\n",num_vars)


# dashboardign by graphs
fig , ax =plt.subplots(2,2 ,figsize=(10,10))
# missing Values
sns.heatmap(df.isnull(),ax=ax[0,0])

ax[0,0].set_title("Missing Values Map (Yellow = Missing)")
ax[0,1].bar(['catergorical','numerical'],[len(cat_vars),len(num_vars)])
ax[0,1].set_title('Variable Types Count')
ax[0,1].set_ylabel('Count')



# Data types pie chart
ax[1,0].pie(df.dtypes.value_counts().values,labels=df.dtypes.value_counts().index,autopct='%1.1f%%')
ax[1,0].set_title('Data Types Distribution')

unique_counts = df.nunique().sort_values(ascending=False)

ax[1,1].barh(range(len(unique_counts)),unique_counts.values)
ax[1,1].set_yticks(range(len(unique_counts)))
ax[1,1].set_yticklabels(unique_counts.index, fontsize=8)
ax[1,1].set_title('Unique Values per Column')
ax[1,1].set_xlabel('Unique Values Count')
plt.tight_layout()
plt.show()

