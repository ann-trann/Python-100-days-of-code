################### Scope ####################

enemies = 1

def incresae_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

incresae_enemies()
print(f"enemies outside function: {enemies}")

#Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3
def create_enemies():
    enemies ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"





########################################### The Number Guessing Game ###########################################
################################################### My code ####################################################


import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

rand_number = random.randint(1, 100)
print(rand_number)

choose_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game_on(choose_mode):
    if choose_mode == 'easy':
        time = 10
    elif choose_mode == 'hard':
        time = 5

    while time > 0:
        print(f"You have {time} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if guess_number > rand_number:
            print("Too high.")
        elif guess_number < rand_number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {rand_number}")
            return
        time -= 1
        if time:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose.")


game_on(choose_mode)




################################################### Angela Yu code ################################################

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's gues against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make the function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turn s and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

