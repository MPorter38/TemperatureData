# Exploratory Analysis of Cities Avg Temps

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AvgTemps.csv", header =0, index_col=0 )

#Dimensions 
print(f'This database has', df.shape[0], "countries")
# Histogram
df.hist()
plt.ylabel("Frequency")
plt.xlabel("Average Temp")
plt.title("Histogram of Average Temperatures")
plt.show()

# Min and Max
print(f'Country with highest avg temp is', df["Cities"][df["Temp"].idxmax()],'with a temp of', df["Temp"].max())
print(f'Country with highest avg temp is', df["Cities"][df["Temp"].idxmin()],'with a temp of', df["Temp"].min())

# Mean, Median, Range
print(f'The mean avg temp is', df["Temp"].mean())
print(f'The median avg temp is', df["Temp"].median())
print(f'The range of the avg temp is', df["Temp"].max()- df["Temp"].min())

# Standard deviation
print(f'The standard deviation in avg temp is', df["Temp"].std())

# How many countries are within x degrees of each others avg temp?
# Try method with max temp country 
max_temp = df["Temp"].max()
max_neighbours_count = 0
max_neighbours = [] 
for c,i in enumerate(df["Temp"]):
    if abs(i - max_temp) < 1:
        max_neighbours_count += 1
        max_neighbours.append(df["Cities"].iloc[c])
print(f'There are', max_neighbours_count, 'countries that have an average within 1 degree of the max. These are', max_neighbours)

# Try method with min temp country 
min_temp = df["Temp"].min()
min_neighbours_count = 0
min_neighbours = [] 
for c,i in enumerate(df["Temp"]):
    if abs(i - min_temp) < 5:
        min_neighbours_count += 1
        min_neighbours.append(df["Cities"].iloc[c])
print(f'There are', min_neighbours_count, 'countries that have an average within 5 degree of the max. These are', min_neighbours)