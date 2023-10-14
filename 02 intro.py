import pandas
import pandas as pd # we can also use the alias as to represent in smaller form

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

print(pd.__version__) # checking the pandas version
