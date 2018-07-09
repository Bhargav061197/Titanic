import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#To check style available
plt.style.available

# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')

#The seed during such random number generation is actually the starting point in the sequence. If we use same seed every time, it will yield same sequence of random numbers.


np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))
#without label "default"
df.plot()
df.plot('A','B', kind = 'scatter')
# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
df.plot.box()
df.plot.hist(alpha=0.7)
df.plot.kde()

#iris is a df

pd.tools.plotting.scatter_matrix(iris);

plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');