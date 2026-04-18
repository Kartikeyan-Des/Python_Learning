import pandas as pd

data = {
    "Name": ["Raj","Ranga","Ramesh","Ramon","Raman"],
    "City": ["Chennai", "Mumbai", "Chennai", "Delhi", "Mumbai"],
    "Salary": [16000,60000,53000,1000,None],
    "Age": [23,45,33,22,None]
}

df =pd.DataFrame(data)



df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print(df.groupby("City")["Salary"].agg(["mean","max","count"]))