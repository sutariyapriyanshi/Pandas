# Import pyplot from Matplotlib and visualize our DataFrame

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot()
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()


#Three lines to make our compiler able to draw
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'hist')
# The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
