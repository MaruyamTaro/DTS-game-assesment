# Import
import random
import time
import os

# Variables
difficulty = 0
day_count = 0

wood = 100
scrap = 10
people = 5
food = 10
current_gear = 0


ITEMS = []
INVENTORY = []


#lists and dictionary
#This will be values that will be used when upgrading
UPGRADES = [
    {"BASE_UPGRADES": [{"wall_1": 0.1, "wall_2": 0.3, "wall_1": 0.4, "wall_1": 0.5}]}
    , {"GEAR_UPGRADES": [{"Level 1 gear": 1.2, "Level 2 gear": 1.4, "Level 3 gear": 1.8, "Level 4 gear": 2}]}]
#these are the values that will change depending on the difficulty
EASY = [
        {"CHANCES": [{"zombie": 0.1, "scav_death": 0.1, "food_rate": 0.2, "wood_rate": 200, "scrap_rate": 200, "people_rate": 2, "people_death": 2}]}
       ]

HARD = [
        {"CHANCES": [{"zombie": 0.1}, {"scav_death": 0.2}, {"food_rate": 0.25, "wood_rate": 150, "scrap_rate": 150, "people_rate": 3, "people_death": 3}]}
       ]

UNFAIR = [
        {"CHANCES": [{"zombie": 0.5}, {"scav_death": 0.4}, {"food_rate": 0.4, "wood_rate": 100, "scrap_rate": 100, "people_rate": 5, "people_death": 5}]}
       ]


# Functions
# The Menu Function that gets used in the beginning
def menu():
    global difficulty, EASY, HARD, UNFAIR
    print(
        "This is a Base building game set in a zombie apocalypse!\nTo win you have to survive 100 days!\nUpgrade your gear to scavenge more materials and protect your base!")
    playerInput = input("What difficulty do you want to play! (1 for Easy) (2 for Hard) (3 for unfair)\n")

    if playerInput == "1":
        difficulty = EASY

    if playerInput == "2":
        difficulty = HARD

    if playerInput == "3":
        difficulty = UNFAIR
    try:
        player_input = input("If you want to play, press 1. If you want to quit press 2\n")
        if player_input == "1":
            os.system('cls')
            game()
        if player_input == "2":
            quit()
    except ValueError:
        print("Invalid input Try again")


def game():
    print("You wander around with your team and finally found a place you can stay and make camp\nYou Can go scavenging for people, scrap, and wood. Per day your food will go down depending on the number of people\n"
          "you will need to upgrade your gear for more materials scavenging and upgrade your base to defend from raids.")
    input("Press Enter to continue...")
    os.system('cls')
    print("you start off with " + str(people) + " people, " + str(wood) + " wood, " + str(scrap) + " scrap, and " + str(food) + " food.")
    day()




#function for player to upgrade gear and Base with materials.
def upgrade():
    print("you need materials to upgrade your Gear and Base")





#player gaining materials after scavenging
def generator():
    global wood, scrap, people, food
    #this part finds out how much of each materials are getting found
    wood_found = random.randint(10, difficulty[0]["CHANCES"][0]["wood_rate"])
    scrap_found = random.randint(10, difficulty[0]["CHANCES"][0]["scrap_rate"])
    people_found = random.randint(0, difficulty[0]["CHANCES"][0]["people_rate"])
    people_dead = people-random.randint(0, difficulty[0]["CHANCES"][0]["people_death"])
    people = people-people_dead
    print("you scavenged for a few hours in a close city with leftover loot")
    if people_dead >= 0:
        print("Unfortunately ", people_dead, " people died")

    print("With the tools you have today, you scavenged " + str(wood_found) + " wood and " + str(scrap_found) + " scrap and you found " + str(people_found))
    print("After a long day of scavenging you go home to rest and prepare for the next day.")
    input("Press Enter to continue...")
    day()


def day():
    global day_count,food
    #calculates how much food per day
    food_per_day = difficulty[0]["CHANCES"][0]["food_rate"]
    food -= people * food_per_day
    day_count += 1
    print("This is day ", int(day_count))
    print("Your team ate", str(food), "kilos of food today")
    print("you Have " + str(people) + " people, " + str(wood) + " wood, " + str(scrap) + " scrap, and " + str(food) + " food.")
    try:
        playerInput = int(input("Do you want your team to go scavenging for materials? Some might die. 1 for scavenging  2 for upgrades\n"))
        if playerInput == 1:
            os.system('cls')
            generator()

        elif playerInput == 2:
            os.system('cls')
            upgrade()

    except ValueError:
        print("Invalid input Try again")



    while food >= 0 or people >= 0 or day_count >= 100:
        day()
    if food <= 0:
        print("Everyone starved. You lose")
        input("Press Enter to continue...")

    elif people <= 0:
        print("you have no more people left. You lose")
        input("Press Enter to continue...")

    if food >= 0 and people >= 0 and day_count >= 100:
        print("You win! you survived for 100 days!")
        input("Press Enter to continue...")



# Main
menu()
