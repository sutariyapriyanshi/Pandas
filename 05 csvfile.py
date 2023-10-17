# Load a comma separated file (CSV file) into a DataFrame

import pandas as pd

df = pd.read_csv('data.csv')
print(df) # it will return the dataset item in which first and last 5 item are only shown
print("\n")
print(df.to_string()) # it will return the whole data

print(pd.options.display.max_rows) # Check the number of maximum returned rows:

# Increase the maximum number of rows to display the entire DataFrame

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 
