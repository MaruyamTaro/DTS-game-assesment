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
# The Menu Function that gets used in the beginning
def menu():
    global difficulty
    print(
        "This is a Base building game set in a zombie apocalypse!\nTo win you have to survive 100 days!\nUpgrade your gear to scavenge more materials and protect your base!")
    difficulty = input("What difficulty do you want to play! (1 for Easy) (2 for Hard) (3 for unfair)")

    player_input = input("If you want to play, press 1. If you want to quit press 2")
    if player_input == "1":
        game()
    if player_input == "2":
        quit()


def game():
    print("you start off with " + str(people) + " people " + str(wood) + " wood." + str(scrap) + "scrap and " + str(
        food) + " food.")
    while food >= 0 or people >= 0 or day_count >= 100:
        day()
    if food >= 0:
        print("Everyone starved. You lose")

    elif people >= 0:
        print("you have no more people left. You lose")

    if food >= 0 and people >= 0 and day_count >= 100:
        print("You win! you survived for 100 days!")



#function for player to upgrade gear and Base with materials.
def upgrade():
    print("you can upgrade your Gear and Base!")






def generator():  #player gaining materials after scavenging
    global wood, scrap, people, food
    wood_found = 0
    scrap_found = 0
    people_found = 0

    print(
        "With the tools you have today you scavenged " + wood_found + "wood and " + scrap_found + "scrap and you found " + people_found)


def day():
    global day_count
    day_count += 1
    print("This is day ", int(day_count))
    try:
        playerInput = int(input("Do you want your team to go scavenging for materials? Some might die. 1 for Yes 2 for no"))
        if playerInput == 1:
            generator()

        elif playerInput == 2:
            upgrade()

    except ValueError:
        print("Invalid input Try again")


# Main
menu()
