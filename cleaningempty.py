# Return a new Data Frame with no empty cells

import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna() # By default, the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string())

df.dropna(inplace = True) # Remove all rows with NULL values
# If you want to change the original DataFrame, use the inplace = True argument
print(df.to_string())

df.fillna(130, inplace = True) # Replace NULL values with the number 130
print(df.to_string())

# Replace Only For Specified Columns
df["Calories"].fillna(130, inplace = True) # Replace NULL values in the "Calories" columns with the number 130

# Replace Using Mean, Median, or Mode

df = pd.read_csv('data.csv')
x = df["Calories"].mean() # Calculate the MEAN, and replace any empty values with it
df["Calories"].fillna(x, inplace = True)
x = df["Calories"].median() # Calculate the MEDIAN, and replace any empty values with it
df["Calories"].fillna(x, inplace = True)
x = df["Calories"].mode()[0] # Calculate the MODE, and replace any empty values with it
df["Calories"].fillna(x, inplace = True)
print(df.to_string())