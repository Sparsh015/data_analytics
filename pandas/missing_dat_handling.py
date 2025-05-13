import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/Spars/Downloads/customers-100.csv")

print(data.isnull().sum())

#to fill null data with something 

#this data.replace will replace all null values with 30000 but what if the null values are in name or gender then integer data doesnt make sene
print(data.replace(np.nan,30000))

data["First Name"] = data["First Name"].replace(np.nan, "NO NAME")

#if want to replace Nan values like for example if in salary column then replace it by them mean of that colums so that it retains the math of the colums
#example
#           avg = data["salary"].mean()
# and then
#           data["salary"] = data["salary"].replace(np.nan,avg)) 


#to fill nan value by just the value above it (forward fill "fill")
data.fillna(method = "ffill")

#to fill nan value by just the value below it (backward fill "bill")
data.fillna(method = "bfill")

