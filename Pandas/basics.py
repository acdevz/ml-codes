import pandas as pd

""" Data Structures """
# Series
s = pd.Series([1, "2", 3, 4], index=['a', 'b', 'c', 'd']);
print(s);

# DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]]);
print(df);