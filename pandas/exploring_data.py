import pandas as pd

data = pd.read_excel("D:/Python/data_analytics/IIT_R UNGA.xlsx")
#if the data is huge then in jupyter nb not all values display
#it hows the starting and last 5 values
print(data)

#to know more data
print(data.head(10))
print(data.tail(10))

#to know the data types of the data 
print(data.info)

#shows info like std, mean, min, and percentiles
data.describe()

#to know where the data has null values
print(data.isnull())

#to know the Count of null values per colulm
print(data.isnull().sum())

