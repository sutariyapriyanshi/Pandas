import pandas as pd

df = pd.read_csv('data.csv') # convert to date
df['Date'] = pd.to_datetime(df['Date']) # convert all cells in the 'Date' column into dates Pandas has a to_datetime() method
print(df.to_string())

# Remove rows with a NULL value in the "Date" column
df.dropna(subset=['Date'], inplace = True)
