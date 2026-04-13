import pandas as pd

data = {
    "Name": ["Raj","Ranga","Ramesh","Ramon","Raman"],
    "City": ["Chennai", "Mumbai", "Chennai", "Delhi", "Mumbai"],
    "Salary": [16000,60000,53000,1000,None],
    "Age": [23,45,33,22,None]
}

df =pd.DataFrame(data)

print(df)
print("=========")
print(df.info())
print("=========")
print(df.describe())