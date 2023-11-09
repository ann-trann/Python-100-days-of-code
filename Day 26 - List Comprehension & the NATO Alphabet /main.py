# # For loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)
#
# # # List Comprehension
# # new_list = [new_item for item in list]
#
# new_list_2 = [n + 1 for n in numbers]
# print(new_list_2)
#
# # String as List
# name = "Angela"
# new_list_3 = [letter for letter in name]
# print(new_list_3)
#
# # Python Sequences: list, range, string, tuple
# # Range as LIst
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)
#
#
# # # Conditional List Comprehension
# # new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
#
# long_uppercase_name = [name.upper() for name in names if len(name) > 5]
# print(long_uppercase_name)


#########################################################################


# # Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {
    student: random.randint(1, 100) for student in names}
print(students_scores)

passed_student = {
    student: score
    for (student, score) in students_scores.items() if score >= 50}
print(passed_student)
