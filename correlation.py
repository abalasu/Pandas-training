import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

stu_df = pd.read_csv("D:\PythonData\student_percentage.csv")
corr = stu_df.corr()
sns.heatmap(corr,xticklabels=corr.columns, yticklabels=corr.columns)
plt.show()
