import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(10)) # Get a quick overview by printing the first 10 rows of the DataFrame
print(df.head()) # Print the first 5 rows of the DataFrame
print(df.tail()) # Print the last 5 rows of the DataFrame
print(df.info()) # Print information about the data
