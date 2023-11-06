
'''
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breath()
'''


##################################################################

'''
class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True
        self.temperament = "friendly"

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")


doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

'''

######################################################################

piano_keys = ["a", "b", "c", " d", "e", "f", "g"]

# print(piano_keys[2:5])
# print(piano_keys[2:])
# print(piano_keys[:5])
# print(piano_keys[2:5:2])
# print(piano_keys[::2])
# print(piano_keys[::-1])

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[2:5])
