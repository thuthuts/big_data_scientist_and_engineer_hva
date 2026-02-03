import pandas as pd
#1. Read the file IMDB.csv into a pandas dataframe
imdb_df = pd.read_csv('Big Data Scientist and Engineer/Workshop2/IMDb movies.csv')
print(len(imdb_df))
print(imdb_df['genre']) 

#2. Select only rows with USA $ sign
print(imdb_df['budget'])
dollar_rows = imdb_df[~imdb_df['budget'].isna()]
print(dollar_rows['budget'])

dollar_rows = dollar_rows[dollar_rows['budget'].str.contains("\$")]
print(dollar_rows['budget'])
print(dollar_rows)


#3. Remove the $ sign
dollar_rows['budget'] = dollar_rows['budget'].str.replace("$", "")
print(dollar_rows['budget'])
print(len(dollar_rows))

#4. Make the type numerical
dollar_rows['budget'] = dollar_rows['budget'].astype('int')


#5. Make a (bar) plot where for each year you could see the total budget
print(dollar_rows.columns)
plot_data = pd.DataFrame({"budget": dollar_rows['budget']}, index= dollar_rows['year'])
plot_data.plot(kind="bar")
import matplotlib.pyplot as plt
plt.show()