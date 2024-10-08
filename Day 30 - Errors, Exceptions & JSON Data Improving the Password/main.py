# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_value"]

# # IndexValue
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# # Exception Handling
# try: something that might cause an exception
# except: do this if there was an exception
# else: do thies if there were no exceptions
# finally: do this no matter what happens

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdf"])  # Cause error but there's no warning
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("File was closed.")
    raise KeyError("This is an error that I made up.")


# BMI Example
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / (height ** 2)
print(bmi)
