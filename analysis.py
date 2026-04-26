import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

plt.plot(df["temperature"])
plt.title("Temperature Trend")
plt.show()