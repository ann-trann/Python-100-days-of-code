# # LESSON 28 -  DAY 26 - SQUARING NUMBERS
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)


# LESSON 29 - DAY 26 - FILTERING EVEN NUMBERS
list_of_strings = input().split(',')
# TODO: Use list comprehension to convert the strings to integers 👇:
int_list = [int(n) for n in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers and store the even numbers in a list called "result"
result = [n for n in int_list if n % 2 == 0]
print(result)
# input: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
