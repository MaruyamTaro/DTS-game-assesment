# Import
import random

# Variables
difficulty = 0
day_count = 0
wood = 100
scrap = 10
people = 5
food = 10


# lists and dictionary

# Functions
def menu():
    global difficulty
    print("This is a Base building game set in a zombie apocalypse")
    difficulty = input("What difficulty do you want to play! (1 for Easy) (2 for Hard) (3 for unfair)")
    player_input = input("If you want to play, press 1. If you want to quit press 2")
    if player_input == "1":
        game()
    if player_input == "2":
        quit()


def game():
    print("you start off with " + str(people) + " people " + str(wood) + " wood." + str(scrap) + "scrap and " + str(
        people) + " people.")

def day():
    global day_count
    day_count += 1
    print("This is day " + int(day_count))
    pass
def generator():
    global wood, scrap, people, food
    print("Today you scavenged " + wood + "wood and " + scrap + "scrap and you found " + people)




# Main
#menu()
#generator()
day()