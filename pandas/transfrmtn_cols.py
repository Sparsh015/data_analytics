import pandas as pd
data = pd.read_excel("D:/Python/data_analytics/IIT_R UNGA.xlsx")

#to add an additional column ad its values according to condition
data.loc[(data["MOD 1 (10)"] > 5.70), "marks"] = "good"
data.loc[(data["MOD 1 (10)"] <= 5.70), "marks"] = "okayish"

print(data)

data["country-marks"] = data["Countries"] +" "+ data["marks"].str.capitalize()
print(data.head(10))

#dictionary
data2 = {"Months":["January","February","March","April"]}

a = pd.DataFrame(data2)
print(a)

def extract(value):
    return value[0:3]

a["Full_months"] = a["Months"].map(extract)
print(a)