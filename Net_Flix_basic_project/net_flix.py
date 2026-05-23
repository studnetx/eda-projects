import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.style.use('seaborn-v0_8-poster')
df = pd.read_csv('../data/mymoviedb.csv',lineterminator='\n')
# overview of data
df.shape
df.info()
df.describe()
# 1.cheacking duplicates
# 2.cheacking null
df.isnull().sum() 
df.duplicated()
# removing unecessary details 
df.drop(['Original_Language',"Overview","Poster_Url"],axis=1,inplace=True)
# changin the data type
df['Release_Date']=pd.to_datetime(df['Release_Date']).dt.year
# spliting the genre by ','
df['Genre']=df['Genre'].str.split(', ')
# create row for multiple name genre
df=df.explode('Genre')
df['Genre']=df['Genre'].astype('category')

# most freqeny genre of movies
genre_name=df['Genre'].value_counts().index
genre_count=df['Genre'].value_counts().sort_values(ascending=False).values
plt.barh(genre_name,genre_count,color='steelblue')
plt.Figure(figsize=(18,9))
plt.xticks(rotation=0)
plt.title("Most Frequest Genre",pad=35)
plt.tight_layout()
plt.ylabel('Genre')
plt.xlabel('Counts')
plt.show()

# State of movies 
labels_for_movies=df['Vote_Average'].value_counts().index
count_for_movies=df['Vote_Average'].value_counts().values
plt.barh(labels_for_movies,count_for_movies,color='#4285f7')
plt.xlabel("Counts")
plt.ylabel('Genres')
plt.title("state of movies",pad=30)


# most popular movie
popular_movie=df[df['Popularity']==df['Popularity'].max()]
print("popular_movie: ",popular_movie)
# block movie
block_movie=df[df['Popularity']==df['Popularity'].min()]
print("popular_movie: ",block_movie)

# movies releaes are in which yearr
plt.hist(df['Release_Date'],color='#4287f5')
plt.title("most movies releases",pad=30)
plt.xlabel("Year")
plt.ylabel('frequecy')


#summary
# - Most frequent Genre: In NetFlix The Most frequent Genre is Drama

# - state of movies: The most movies are Popular

# - which movie most popular: Spider-Man: No Way Home and popularity Rate is 5083.954

# - which movie lowes popular: The United States vs. Billie Holiday and popularity Rate 13.354

