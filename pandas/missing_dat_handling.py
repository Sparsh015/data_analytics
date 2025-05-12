import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/Spars/Downloads/customers-100.csv")

print(data.isnull().sum())

#to fill null data with something 

#this data.replace will replace all null values with 30000 but what if the null values are in name or gender then integer data doesnt make sene
print(data.replace(np.nan,30000))

data["First Name"] = data["First Name"].replace(np.nan, "NO NAME")

