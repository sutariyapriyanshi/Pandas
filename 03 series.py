# Create a simple Pandas Series from a list

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0]) # Return the first value of the Series

# Create your own labels

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"]) # Return the value of "y"

# Create a simple Pandas Series from a dictionary

calories = {"day1": 420, "day2": 380, "day3": 390} # Key/Value Objects as Series
myvar = pd.Series(calories)
print(myvar)

# Create a Series using only data from "day1" and "day2"

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# Create a DataFrame from two Series

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
