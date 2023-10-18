import pandas as pd

df = pd.read_csv('data.csv')
print(df.duplicated()) # To discover duplicates, we can use the duplicated() method
# The duplicated() method returns a Boolean values for each row

df.drop_duplicates(inplace = True) # Remove all duplicates
