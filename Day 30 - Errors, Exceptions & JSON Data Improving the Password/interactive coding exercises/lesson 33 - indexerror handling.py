# LESSON 33 - DAY 30 - INDEXERROR HANDLING
# input: ["Apple", "Pear", "Orange"]

# Convert formatted string to list
fruits = eval(input())


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(2)  # Raises IndexError on list with less than 5 items.
