import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("score.csv")
df["Score"] = df.mean(axis=1)

plt.plot(df["Score"], range(len(df)))



plt.show()