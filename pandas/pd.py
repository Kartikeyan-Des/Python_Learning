import pandas as pd

data = {
    'Student_ID': [101,102,103,104],
    'Name': ['Tomy', 'Alex', 'Sarah', 'Nicola'],
    'Grade': [90, 60, 89, 100],
    'City': ['Chennai', 'Mumbai', 'Hyderabad', 'Bengaluru']
}

df = pd.DataFrame(data)

# df.to_csv('student.csv', index=False)

# print("CSV Created Successfully")

# print(df.head(2))

# high_grades = df[df['Grade'] > 90]
# print(high_grades)

df['Passed'] = df['Grade'] > 80
print(df)