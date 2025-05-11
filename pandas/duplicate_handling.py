import pandas as pd

data = pd.read_excel("D:/Python/data_analytics/IIT_R UNGA.xlsx")
print("data\n",data)

# duplicate values in row
print(data.duplicated())

print()

##### ALWAYS USE PRIMARY KEY TO HANDLE DUPLICATES

#duplicate value in columm
print(data["Countries"].duplicated())

#count of duplicate data
print(data["Countries"].duplicated().sum())

#to remove duplicate values based on column name
print(data.drop_duplicates("MOD 1 (10)"))