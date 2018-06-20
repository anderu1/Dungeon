#This section controls the Main Menu
def Run_Menu():
    global x_loc
    global y_loc
    global location
    global X
    global town_level
    print("")
    print("Welcome to Dungeon Town")
    print("")
    print("What would you like to do:")
    print("1. New Game")
    print("2. Continue")
    print("3. Credits")
    print ("4. Exit")
    Menu_Choice = input("Please Make a Selection\n")
    if Menu_Choice == "1":
        town_level = 0
        location ="Town"
    elif Menu_Choice == "2":
        x_loc = saved_x_loc
        y_loc = saved_y_loc
        location = saved_loc
    elif Menu_Choice == "3":
        location = "Credits"
    elif Menu_Choice == "4":
        print("Thank you for Playing")
        X = -1
    else:
        location = "Menu"

#This section shows the credits
def Run_Credits():
    global X
    global location
    print("This was made using Python.")
    print("Creator: Andrew Swanson")
    print("1. Return to Menu")
    print("2. Exit")
    user_input = input("Please Make a Selection:\n")
    if user_input == "1":
        location = "Menu"
    elif user_input == "2":
        X = -1
    else:
        location = "Credits"

#This section is the Town Menu
def Run_Town(town_level):
    global x_loc
    global y_loc
    global X
    global location
    global town_name
    #Here is where the towns are named, and what floor is in front or behind them is available
    if town_level == 0:
        town_name = "Beginner Village"
        forward = "Floor1"
        backward = 0
    elif town_level == 1:
        town_name = "First Town"
        forward = "Floor2"
        backward = "Floor1"
        x_loc = 52
        y_loc =52
    #Here is the Town Menu
    print("Welcome to",town_name)
    print("What would you like to do:")
    print("1. General Goods Store")
    print("2. Magic Shop")
    print("3. Enter Next Dungeon Level")
    if backward != 0:
        print("4. Go to Previous Dungeon Level")
        print("5. Exit")
    else:
        print("4. Exit")
    user_input = input("Please Make a Selection:\n")
    if user_input == "1":
        location = "GeneralShop"
    elif user_input == "2":
        location = "MagicShop"
    elif user_input == "3":
        x_loc = 0
        y_loc = 0
        location = forward
    elif user_input == "4" and backward != 0:
        location = backward
    elif user_input == "4" or user_input == "5":
        X = -1

#This section is the Magic shop
def Run_Magic_Shop(town_level, town_name):
    print("Welcome to",town_name,"'s Magic Shop")


    
#This is where the Game Begins
location = "Menu"
X = 1
while X != -1:
    if location == "Menu":
        Run_Menu()
    elif location == "Town":
        Run_Town(town_level)
    elif location == "Floor1":
        Run_Floor1(x_loc, y_loc)
    elif location == "MagicShop":
        Run_Magic_Shop(town_level, town_name)
    elif location == "GeneralShop":
        Run_General_Shop(town_level, town_name)
    elif location == "Credits":
        Run_Credits()
