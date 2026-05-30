import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data set
df=sns.load_dataset("tips")


# Distribution of total bills
# What is the most common total bill range?
# How does the distribution differ between lunch and dinner?

fig ,ax =plt.subplots(figsize=(16,8))
ax.hist(df['total_bill'],bins=15, edgecolor='black', alpha=0.7,density=True)
ax.set_xlabel("Bills")
ax.set_ylabel("counts")
ax.set_title("Common Bill Range")
plt.show()

# total_bill  of lunch vs dinner
fig , ax= plt.subplots(ncols=2,nrows=1)
# dinner Time 
dinnerdf=df[df['time']=='Dinner']
Lunchdf=df[df['time']=='Lunch']
ax[0].hist(dinnerdf['total_bill'],bins=30,color='skyblue', edgecolor='black', alpha=0.7)
ax[1].hist(Lunchdf['total_bill'],bins=30,color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Distibution of Bills by Dinner and Lunch")
plt.savefig('../pictures/bill_at_dinner_lunch.png')
plt.show()
