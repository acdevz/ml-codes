import pandas as pd

""" Data Structures """
# Series - 1D array
s = pd.Series([1, "2", 3, 4], index=['a', 'b', 'c', 'd']);
print(s);

# DataFrame - 2D labelled Data Structure with columns of potentially different types
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]]);
print(df);