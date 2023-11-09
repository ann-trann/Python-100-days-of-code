# # LESSON 31 - DAY 26 - DICTIONARY COMPREHENSION 1
# # Create a dictionary that takes each word in the given sentence
# # and calculates the number of letters in each word.
# # input: What is the Airspeed Velocity of an Unladen Swallow?
#
# sentence = input()
# # Using dictionary comprehension
# result = {word: len(word) for word in sentence.split()}
# print(result)


###################################################################################


# LESSON 32 - DAY 26 - DICTIONARY COMPREHENSION 2
# Create a dictionary that takes each temperature in degrees Celsius
# and converts it into degrees Fahrenheit.
# input: {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# eval() converts correctly formatted string to dict
weather_c = eval(input())

# dictionary comprehension
weather = {print(day, temp) for (day, temp) in weather_c.items()}
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)
