student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a frame
for (index, row) in student_data_frame.iterrows():
    print(index)
print("\n")
for (index, row) in student_data_frame.iterrows():
    print(row)
print("\n")
for (index, row) in student_data_frame.iterrows():
    print(row.score)
print("\n")

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

####################################################################

'''

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

'''
