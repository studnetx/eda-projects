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
# Avg Tip by Day
grouped=df.groupby('day',observed=False)['tip']
tip_mean=grouped.mean()
tip_std=grouped.std()
tip_len=grouped.count()
tip_day=grouped.mean().index
sem=tip_std/np.sqrt(tip_len)
plt.bar(tip_day,tip_mean,yerr=sem,capsize=5)
plt.xlabel('Day')
plt.ylabel('Average Tip ($)')
plt.title('Average Tip by Day with Standard Error')
plt.savefig('../pictures/Average_tip_by_day.png')
plt.show()
# Tips 
df["percentage_tip"]=(df['tip']/df['total_bill'])*100
grouped=df.groupby('size')['percentage_tip'].agg(['mean','std','count'])
grouped['sem']=grouped['std']/np.sqrt(grouped['count'])
grouped
fig ,ax=plt.subplots()
ax.errorbar(grouped.index , grouped['mean'],yerr=grouped['sem'],marker='o', capsize=5, linestyle='-', color='blue')
ax.set_xlabel('Party Size')
ax.set_ylabel('Average Tip Percentage (%)')
ax.set_title('Tip Percentage by Party Size')
ax.grid(True, linestyle=':', alpha=0.7)
plt.savefig('../graphs/tip_per_by_party_size.png')
plt.show()

# Tip distribution by time of day
fig ,ax=plt.subplots()
data_to_plot = [df[df['time'] == 'Lunch']['tip'],
                df[df['time'] == 'Dinner']['tip']]

ax.boxplot(data_to_plot,tick_labels=['Lunch','Dinner'])
ax.set_ylabel('Tip ($)')
ax.set_title('Tip Distribution by Time of Day')
plt.savefig('../graphs/tip_at_dinner&lunch.png')
plt.show()

# Number of customers by day and time

