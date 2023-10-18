import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())

# Perfect Correlation:
# number 1.000000, which makes sense, each column always has a perfect relationship with itself.

# Good Correlation:
# 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, 
# and the other way around

# Bad Correlation:
# 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of 
# the work out, and vice versa.
