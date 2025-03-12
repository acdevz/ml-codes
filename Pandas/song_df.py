import pandas as pd

""" From CSV """
df = pd.read_csv('X:\\__codes__\\ML\\Pandas\\data\\songs_stats.csv');
# print(df)

""" From JSON """
# df = pd.read_json('X:\\__codes__\\Python\\Pandas\\data\\songs_stats.json');
# print(df)

""" From Dictionary """
# df = pd.DataFrame({
#     "title": ["willow", "champagne problems", "gold rush", "august"],
#     "artist": ["Taylor Swift", "Taylor Swift", "Taylor Swift", "Taylor Swift"],
#     "album": ["evermore", "evermore", "evermore", "folklore"],
#     "duration": [208, 240, 208, 208]
# });
# print(df)

""" Functions """
# print(df.head(1)); 
# print(df.tail(1));
# df.info(); # Get information about the DataFrame
# print(df.describe()); # Get statistics about the DataFrame

""" Attributes """
# numpy_arr = df.to_numpy(); # Convert DataFrame to NumPy array
# print(numpy_arr);
# print(df.columns); # Get the column names
    
""" Slicing & Indexing """
# #️⃣ column wise
# print(df['Title']); # Get a column, as a Series 👈
# #️⃣ row wise
# print(df[0:1]); # Get a row
# #️⃣ row and column wise
# print(df[0:][['Title', 'Duration']]); # Get rows and columns

""" Sorting """
print(df.sort_values(by='Duration', ascending=False)); # Sort by a column
# print(df.sort_index(ascending=False)); # Sort by index

""" Filtering """
# print(df[df['Duration'] > 200]); # Filter rows based on a condition

""" Null Values & Duplicates """
print(df.isnull()); # Check for null values
print(df.dropna()); # Drop rows with null values
print(df.fillna(0)); # Fill null values with a value
print(df.drop_duplicates()); # Drop duplicate rows


""" 👉 To read large files into Dataframe, use datatable or dask instead of Pandas to reduce the time taken.
    👉 Use lighter data formats like feather or parquet to save files instead of CSV, as saving in these formats is much faster. """