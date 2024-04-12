# Import allows code that are not in default python for example random functions are not
import random
import math
import os

# Variables hold different types information

# In this project I use variables to store lists and values that get changed in the rest of the code
difficulty = 0
day_count = 0

wood = 0
scrap = 0
people = 8
food = 10

current_gear = 1
current_base = 1
current_gear_cost = 150
current_base_cost = 150

zombie_raid_level = 0

buff = 0

# lists and dictionary holds information like varaiables but can be called and dictonaries are able to set names to different values

# these are the values that will change depending on the difficulty
# I use lists to store values in dictonaires and use it later in the generator function.
EASY = [
    {"CHANCES": [{"zombie": 10, "food_rate": 0.2, "wood_rate": 150, "scrap_rate": 150, "people_rate": 6, "food_find": 3,
                  "people_death": 2}]}
]

HARD = [
    {"CHANCES": [
        {"zombie": 15, "food_rate": 0.25, "wood_rate": 100, "scrap_rate": 100, "people_rate": 5, "food_find": 2,
         "people_death": 3}]}
]

UNFAIR = [
    {"CHANCES": [{"zombie": 20, "food_rate": 0.4, "wood_rate": 75, "scrap_rate": 75, "people_rate": 5, "food_find": 1,
                  "people_death": 3}]}
]


# Functions allow chunks of code that can be called anytime, so you don't have to repeat code
# The Menu Function that gets used in the beginning
# this resets the variables when called and also asks for the difficulty
def menu():
    # global allows the variable to be used and changed in a function
    global difficulty, EASY, HARD, UNFAIR, wood, scrap, people, food, current_gear, current_base, current_gear_cost, current_base_cost, zombie_raid_level, day_count
    difficulty = 0
    day_count = 8


    wood = 0
    scrap = 0
    people = 5
    food = 10

    current_gear = 1
    current_base = 1
    current_gear_cost = 150
    current_base_cost = 150

    zombie_raid_level = 0
    # print function prints strings and variables in the console
    print(
        "This is a Base building game set in a zombie apocalypse!\nTo win you have to survive 100 days!\nUpgrade your gear to scavenge more materials and protect your base!")
    # this code is used many times because this makes the code hard to break.
    # while loops keeps repeating the code while the condition is met or if there is a break in the code
    while True:
        # try tests the code in it and if there is a error the except section handles the error.
        try:
            # input allows the player to make decision in the game by asking for a input
            # I set the input to a variable player_input and use a if statement to do different actions
            player_input = input(
                "What difficulty do you  want to play! (1 for Easy) (2 for Hard) (3 for unfair)(4 to quit)(p to restart)\n")

            # if statements looks at the variable and if the condition is met, does that action.

            if player_input == "1":
                difficulty = EASY
                break
            elif player_input == "2":
                difficulty = HARD
                break
            elif player_input == "3":
                difficulty = UNFAIR
                break
            elif player_input == "4":
                # quit quits the whole code
                quit()

            elif player_input == "p":
                start()
                break
            else:
                print("Invalid")
        except ValueError:
            print("Invalid input Try again")
    game()


def game():
    print(
        "You wander around with your team and finally found a place you can stay and make camp\nYou Can go scavenging for people, scrap, and wood. Per day your food will go down depending on the number of people\n"
        "you will need to upgrade your gear for more materials scavenging and upgrade your base to defend from raids.")
    input("Press Enter to continue...")
    os.system('cls')
    print("you start off with " + str(people) + " people, " + str(wood) + " wood, " + str(scrap) + " scrap, and " + str(
        food) + " food.")
    day()


# function for player to upgrade gear and Base with materials.

def upgrade():
    print("you need materials to upgrade your Gear and Base")
    while True:
        try:
            player_input = input("If you want to upgrade your Gear for better chances at scavenging press 1\n"
                                 "If you want to upgrade your base for higher chances of survival and defence when zombies attack press 2\n(p to restart)\n")
            if player_input == "1":
                upgradegear()
                break
            elif player_input == "2":
                upgradebase()
                break
            elif player_input == "p":
                start()
                break
            else:
                print("Invalid")

        except ValueError:
            print("Invalid input Try again")


# this function gets called when the player wants to upgrade their gear


def upgradegear():
    global wood, scrap, current_gear_cost, current_gear
    # raises the cost of the gear
    cost = current_gear_cost * 1.8
    # round function rounds the cost so there are no floats
    cost = round(cost)
    print("It will take", cost, "scrap and wood to upgrade to the next level.")
    if scrap < cost or wood < cost:  # Changed from 'and' to 'or' because you need to check each resource individually
        input("you don't have enough to upgrade right now\n press enter to go scavenging instead")
        generator()
    else:
        while True:

            try:
                player_input = input("Do you want to spend " + str(
                    cost) + " to upgrade your gear? press 1 for yes press 2 to go scavenging press 3 to go back to select upgrade (p to restart)")
                if player_input == "1":
                    scrap -= cost
                    wood -= cost
                    current_gear += 0.5
                    current_gear_cost = current_gear_cost * 1.5
                    cost = round(current_gear_cost)
                    print("Upgraded to next level\n")
                    break

                elif player_input == "2":
                    generator()
                    break

                elif player_input == "3":
                    upgrade()
                    break

                elif player_input == "p":
                    start()
                    break
                else:
                    print("Invalid")

            except ValueError:
                print("Invalid input Try again")


def upgradebase():
    global wood, scrap, current_base, current_base_cost
    cost = current_base_cost * 1.5
    cost = round(cost)
    print("It will take", cost, "scrap and wood to upgrade to the next level.")
    if scrap < cost or wood < cost:  # Here also change 'and' to 'or'
        input("you don't have enough to upgrade right now\n press enter to go scavenging")
        generator()
    else:
        while True:
            try:
                player_input = input("Do you want to spend " + str(
                    cost) + " to upgrade your base? press 1 for yes press 2 to go scavenging 3 to go back to select upgrade (p to restart)")
                # if player_input == "":
                # continue

                if player_input == "1":
                    scrap -= cost
                    wood -= cost
                    current_base += 1
                    current_base_cost *= 1.5
                    current_base_cost = round(current_base_cost)
                    print("Upgraded to next level\n")
                    break

                elif player_input == "2":
                    generator()
                    break

                elif player_input == "3":
                    upgrade()
                    break

                elif player_input == "p":
                    start()
                    break
                else:
                    print("Invalid input. Please try again.")

            except ValueError:
                print("Invalid input. Please try again.")


# player gaining materials after scavenging
def generator():
    global wood, scrap, people, food

    # used to test the generator
    # print(int(difficulty[0]["CHANCES"][0]["wood_rate"]),int(difficulty[0]["CHANCES"][0]["scrap_rate"]),int(difficulty[0]["CHANCES"][0]["people_rate"]))

    # this part finds out how much of each material are getting found
    # random randint takes a random number in between 2 numbers or variables.
    # i used it here to pick how much the player was able to find by making the range between the rate - 20 and the rate + 20 and pick a number randomly.
    # finally i multiply that number with the gear buff which can be upgraded by the gear upgrade function by the player.
    wood_found = random.randint(int(difficulty[0]["CHANCES"][0]["wood_rate"]) - 20,int(difficulty[0]["CHANCES"][0]["wood_rate"]) + 20) * current_gear
    scrap_found = random.randint(int(difficulty[0]["CHANCES"][0]["scrap_rate"]) - 20,int(difficulty[0]["CHANCES"][0]["scrap_rate"]) + 20) * current_gear
    people_found = random.randint(int(difficulty[0]["CHANCES"][0]["people_rate"]) - 2,int(difficulty[0]["CHANCES"][0]["people_rate"]) + 2) * current_gear
    people_dead = people - random.randint(0, int(difficulty[0]["CHANCES"][0]["people_death"]))
    food_found = random.randint(int(difficulty[0]["CHANCES"][0]["food_find"]) - 1,int(difficulty[0]["CHANCES"][0]["food_find"]) + 1) * current_gear

    # adds the found resources to the players resources
    wood += wood_found
    scrap += scrap_found
    people += people_found
    food += food_found

    # i round so the number is not a float
    wood = round(wood)
    scrap = round(scrap)
    people = round(people)
    food = round(food)
    round(people_dead)
    people = people - people_dead
    print("you scavenged for a few hours in a close city with leftover loot")
    if people_dead >= 0:
        print("Unfortunately ", people_dead, " people died")

    print("With the tools you have today, you scavenged " + str(wood_found) + " wood and " + str(
        scrap_found) + " scrap and you found " + str(people_found), " people")


def Raid():
    global wood, scrap, food, people, current_base, zombie_raid_level
    #makes the raid harder every time
    zombie_raid_level += 2
    # changes the difficulty

    difficulty_multiplier = 1.8  # default is easy
    if difficulty == HARD:
        difficulty_multiplier = 2
    elif difficulty == UNFAIR:
        difficulty_multiplier = 2.5

    print(
        "A horde of zombies is approaching!!")
    # calculate the win probability

    # difficulty multiplier works well and decreases the probability slightly

    win_probability = current_base / (current_base + zombie_raid_level * difficulty_multiplier)
    # this maxes the win probability to 1 so the percentage can't be something like 300 percent
    # max() works by selecting the smaller number in the brackets. max works the same way but picks the bigger number
    win_probability = max(0, min(1, win_probability))

    print(f"Your chance of defending against the raid without losses is {win_probability * 100:.2f}%.")

    # asks what the player wants to do if it is not the last raid (don't want the player to be able to half resource to survive and win)
    if day_count != 50:
        while True:
            decision = input("Do you want to sacrifice 70% of your materials to ensure safety? or risk it and defend your base. you don't lose any resources if you win 1 for yes and 2 for no):p to restart whole game\n ")
            try:
                if decision == "1":
                    # halves all resources
                    wood *= 0.7
                    scrap *= 0.7
                    food *= 0.7
                    people *= 0.7
                    wood = round(wood)
                    scrap = round(scrap)
                    people = round(people)
                    food = round(food)

                    print("You've sacrificed 70% of your materials to survive the raid.")
                    input("enter to continue...")
                    break
                elif decision== "2":
                    # Player takes a risk and a random check is made to see if they win or lose
                    if random.random() < win_probability:
                        # player wins the raid
                        print("You've successfully defended the raid without any losses!")
                        input("enter to continue...")
                        break
                    else:
                        # player loses and gets 90 percent removed
                        wood *= 0.1
                        scrap *= 0.1
                        food *= 0.1
                        people *= 0.1
                        wood = round(wood)
                        scrap = round(scrap)
                        people = round(people)
                        food = round(food)
                        print(
                            "The raid was devastating, you've lost 80% of your materials and people but you still survived.")
                        input("enter to continue...")
                        break
                        #lower() makes the string in to a lowercase letter so if the player put in P it will still work
                elif decision.lower() == "p":
                    start()
                    break

                else:
                    print("invalid")

            except ValueError:
                print("Invalid input. Please try again.")
    else:
        #calls if it is the last day
        print("This is your last day so you can't use half your resources to survive. you need to survive to ba able to go to a safe zone and win the game")
        input("enter to continue and see if you survived")
        # Player takes a risk and a random check is made to see if they win or lose
        if random.random() < win_probability:
            # player wins the raid
            print("You've successfully defended the raid without any losses!")
            print("You win! you survived for 50 days! you got rescue")
            input("enter to continue...")


        else:
            #player loses
            print("you and the team were fighting for hours but unfortunately you lost the raid")
            print("you survived for so long and was one more day off of getting rescued but failed")
            print("you lose")
            input("enter to continue...")


def day():
    os.system('cls')
    global day_count, food
    day_count += 1

    # Check if it's a raid day (every 10 days) by using modolulo function which calculates the remainder of an equation
    if day_count % 10 == 0:
        Raid()

    else:
        print("This is day ", int(day_count))
        print("you Have " + str(people) + " people, " + str(wood) + " wood, " + str(scrap) + " scrap, and " + str(
            food) + " food.")
        print(
            "your current gear is level " + str(current_gear) + " and your current base level is " + str(current_base))
        while True:
            try:
                player_input = int(input(
                    "Do you want your team to go scavenging for materials? Some might die. 1 for scavenging  2 for upgrades\nYOU CAN ONLY DO ONE A DAY\npress p to restart game\n"))
                print(player_input)
                if player_input == 1:
                    generator()
                    break

                elif player_input == 2:
                    upgrade()
                    break

                elif player_input == "p":
                    start()
                    break

                else:
                    print("Invalid")

            except ValueError:
                print("Invalid input Try again")
        # calculates how much food per day is eaten
        food_per_day = difficulty[0]["CHANCES"][0]["food_rate"]
        food -= people * food_per_day
        food = math.ceil(food)

        food_per_day = people * food_per_day
        # imported math so im able to use ceil which rounds up
        food_per_day = math.ceil(food_per_day)

        print("Your team ate", str(food_per_day), "kilos of food today")
        print("After a long day of work you go to rest and see if you have enough food to survive the next day.")
        input("Press Enter to continue...")


def lost():
    if food <= 0:
        print("Everyone starved. You lose")
        input("Press Enter to continue...")

    elif people <= 0:
        print("you have no more people left. You lose")
        input("Press Enter to continue...")

    playagain()


def playagain():
    while True:
        try:
            player_input = int(input(
                "Do you want to try again? press 1 to play again with  different difficulty or press 2 to quit\n"))
            if player_input == 1:
                os.system('cls')
                start()
                break


            elif player_input == 2:
                os.system('cls')
                quit()

            else:
                print("Invalid")
        except ValueError:
            print("Invalid input Try again")


def start():
    menu()
    while food >= 0 or people >= 0:
        if day_count == 50:
            playagain()
        else:
            day()



    if food <= 0:
        lost()



    elif people <= 0:
        lost()


# Main code
start()
