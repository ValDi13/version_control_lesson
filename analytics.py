#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#create dataFrame from dictionary
df = pd.DataFrame({'Name': ['Olena', 'Maks', 'Slava'], 'Age': [23, 34, 45]})
#print of head
#print(df.head())
sns.barplot(data=df, x='Name', y='Age')
plt.show()