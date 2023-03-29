# age = 30
# name = "Felex"
# print(f"{name}")
# age = input("Age:")
# name = input("Name:")

# madlib = f"My name is {name} and and am  {age} year old"
# print(madlib)
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f"Guess a number btwn 1 and {x}:")
        if guess < random_number:
            print("sorry gueess again, Too Low")
        elif guess > random_number:
            print("sorry gueess again, Too High")
    print(f"Yay you have guess correct number {random_number}")


guess(10)
