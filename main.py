#Import
import random


#Variables
difficulty = 0
wood = 100
scrap = 100
people = 5
food = 10


#Functions
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
    global wood, scrap, people, food
    print("you start off with " + str(people) + " people." + str(wood) + " woods." + str(scrap) + "scrapes and " + str(people) + " people.")



#Main
Menu()