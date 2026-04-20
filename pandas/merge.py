import pandas as pd

employees = {
    'EmpID' : [1,2,3,4,5],
    'Name' : ['Raj','Priya','Arun','Sneha','Kiran'],
    'DeptID' : [101,102,101,103,999],
    'Salary' : [45000, 62000, 38000, 71000, 55000],
    'Gender' : ['Male', 'Female', 'Male', 'Female', 'Male']
}

departments = {
    'DeptID' : [101,102,103],
    'DeptName' : ['Engineering','Marketing','Sales'],
    'Location' : ['Chennai','Mumbai','Delhi']
}

df1 = pd.DataFrame(employees)
df2 = pd.DataFrame(departments)


# pivot = df1.pivot_table(values='Salary', index='DeptID', aggfunc='mean')
# print(pivot)


merged = pd.merge(df1, df2, on="DeptID", how="left")

pivot2 = merged.pivot_table(values='EmpID', index='Location',  aggfunc= 'count' )
print(pivot2)