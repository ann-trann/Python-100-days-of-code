# # open and clode file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # open file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # write, replace
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# # append
# with open("my_file.txt", mode="a") as file:
#     file.write("New text.")

# create new file from scratch
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
