import pandas as pd
data = {"name":["john", "Peter","Lisa"],
        "age":[25,28,31],
        "salary" :[300000,45000,250000]}

df = pd.DataFrame(data)
print(df)

#to read from already existing csv file

#data1 = pd.read_csv("file path (change backward slashes to forward slashes)")

#data2 = pd.read_excel(" C:/Users/Spars/OneDrive/Documents/Sponser_list_finalll.xlsx")
#print(data2)
