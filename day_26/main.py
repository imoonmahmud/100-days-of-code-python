import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
lst = []

for (index, row) in student_data_frame.iterrows():
    lst.append(row.student)
    lst.append(row.score)
print(lst)