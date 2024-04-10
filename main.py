# Import
import random
import time
import os

# Variables
difficulty = 0
day_count = 0

wood = 100
scrap = 100
people = 5
food = 10

current_gear = 1
current_base = 1
current_gear_cost = 100
current_base_cost = 100


ITEMS = [{"Name": "worn Ak 47","buff":20}]
INVENTORY = []


#lists and dictionary
#This was the code for the upgrades but i thought that a
#UPGRADES = [
    #{"BASE_UPGRADES": [{"wall_1": 0.1, "wall_2": 0.3, "wall_1": 0.4, "wall_1": 0.5}]}
    #, {"GEAR_UPGRADES": [{"Level 1 gear": 1.2, "Level 2 gear": 1.4, "Level 3 gear": 1.8, "Level 4 gear": 2}]}]
#these are the values that will change depending on the difficulty
EASY = [
        {"CHANCES": [{"zombie": 0.1, "food_rate": 0.2, "wood_rate": 200, "scrap_rate": 200, "people_rate": 2, "people_death": 2}]}
       ]

HARD = [
        {"CHANCES": [{"zombie": 0.1, "food_rate": 0.25, "wood_rate": 150, "scrap_rate": 150, "people_rate": 3, "people_death": 3}]}
       ]

UNFAIR = [
        {"CHANCES": [{"zombie": 0.5, "food_rate": 0.4, "wood_rate": 100, "scrap_rate": 100, "people_rate": 5, "people_death": 5}]}
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
    try:
        player_input = input("If you want to upgrade your Gear for better chances at scavenging press 1\n"
                             "If you want to upgrade your base for higher chances of survival and defence when zombies attack press 2\n")
        if player_input == "1":
            upgradegear()
        elif player_input == "2":
            upgradebase()
        elif player_input == "3":
            return
    except ValueError:
        print("Invalid input Try again")
def upgradegear():
    global wood, scrap, current_gear_cost, current_gear
    cost = 0
    cost = current_gear_cost * 1.5
    print("It will take", cost, "scrap and wood to upgrade to the next level.")
    if scrap and wood <= cost:
        input("you don't have enough to upgrade right now\n press enter to go scavenging instead")
        generator()
    else:
        while True:
            try:
                playerInput = int(input("Do you want to spend "), cost, " to upgrade your gear? press 1 for yes press 2 to go scavenging")
                if playerInput == 1:
                    scrap -= cost
                    wood -= cost
                    current_gear = current_gear * 1.5
                    input("Upgraded to next level\nenter to continue...")
                    break

                elif playerInput == 2:
                    generator()
            except ValueError:
                print("Invalid input Try again")



def upgradebase():
    global wood, scrap, current_base, current_base_cost
    cost = 0
    cost = current_base_cost * 1.5
    print("It will take", cost, "scrap and wood to upgrade to the next level.")
    if scrap and wood <= cost:
        input("you don't have enough to upgrade right now\n press enter to go scavenging")
        generator()
    else:
        while True:
            try:
                playerInput = int(input("Do you want to spend "), cost, " to upgrade your base? press 1 for yes press 2 to go scavenging instead")
                if playerInput == 1:
                    scrap -= cost
                    wood -= cost
                    current_base = current_base * 1.5
                    input("Upgraded to next level\nenter to continue...")
                    break

                elif playerInput == 2:
                    generator()
            except ValueError:
                print("Invalid input Try again")










#player gaining materials after scavenging
def generator():
    global wood, scrap, people, food
    #this part finds out how much of each materials are getting found
    wood_found = random.randint(10, difficulty[0]["CHANCES"][0]["wood_rate"]) * current_gear
    scrap_found = random.randint(10, difficulty[0]["CHANCES"][0]["scrap_rate"]) * current_gear
    people_found = random.randint(0, difficulty[0]["CHANCES"][0]["people_rate"])
    people_dead = people-random.randint(0, difficulty[0]["CHANCES"][0]["people_death"])
    food_found = random.randint(0, people * difficulty[0]["CHANCES"][0]["food_rate"] + 0.5)

    wood += wood_found
    scrap += scrap_found
    people += people_found
    food += food_found

    people = people - people_dead
    print("you scavenged for a few hours in a close city with leftover loot")
    if people_dead >= 0:
        print("Unfortunately ", people_dead, " people died")

    print("With the tools you have today, you scavenged " + str(wood_found) + " wood and " + str(scrap_found) + " scrap and you found " + str(people_found), " people")


def day():
    os.system('cls')
    global day_count,food
    day_count += 1
    print("This is day ", int(day_count))
    print("you Have " + str(people) + " people, " + str(wood) + " wood, " + str(scrap) + " scrap, and " + str(food) + " food.")
    while True:
        try:
            playerInput = int(input("Do you want your team to go scavenging for materials? Some might die. 1 for scavenging  2 for upgrades\nYOU CAN ONLY DO ONE A DAY\n"))
            print(playerInput)
            if playerInput == 1:
                generator()
                break

            elif playerInput == 2:
                upgrade()
                break
        except ValueError:
            print("Invalid input Try again")
    # calculates how much food per day is ate
    food_per_day = difficulty[0]["CHANCES"][0]["food_rate"]

    food -= people * food_per_day
    food_per_day = people * food_per_day

    print("Your team ate", str(food_per_day), "kilos of food today")
    print("After a long day of work you go to rest and prepare for the next day.")
    input("Press Enter to continue...")



#Main
menu()
while food >= 0 or people >= 0 or day_count <= 50:
    day()

    if food <= 0:
        print("Everyone starved. You lose")
        input("Press Enter to continue...")
        break

    elif people <= 0:
        print("you have no more people left. You lose")
        input("Press Enter to continue...")
        break

    if food >= 0 and people >= 0 and day_count >= 50:
        print("You win! you survived for 100 days!")
        input("Press Enter to continue...")
        break

try:
    playerInput = int(input(
        "Do you want to try again? press 1 to play again with  different difficulty or press 2 to quit\n"))
    if playerInput == 1:
        os.system('cls')
        menu()
    elif playerInput == 2:
        os.system('cls')
        quit()
except ValueError:
    print("Invalid input Try again")

