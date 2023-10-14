import pandas as pd

df = pd.read_csv('data.csv')
df.loc[7,'Duration'] = 45 # Set "Duration" = 45 in row 7
print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
# Loop through all values in the "Duration" column
# If the value is higher than 120, set it to 120
print(df.to_string())

# Delete rows where "Duration" is higher than 120

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)