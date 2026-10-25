print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

direction = input("Would you like to turn left or right: L or R")
if(direction.upper() == "L"):
    swim_wait = input("Would like to swim or wait for a boat: S or W")
    if(swim_wait.upper() == "W"):
        door_colour = input("Which door colour would you like to choose: Red, Yellow or Blue?")
        if(door_colour.upper() == "RED"):
            print("You were burnt by fire. Game over!")
        elif(door_colour.upper() == "BLUE"):
            print("You were eaten by beasts. Game over!")
        elif(door_colour.upper() == "YELLOW"):
            print("You won!")
        else:
            print("Game over!")
    elif(swim_wait.upper() == "S"):
        print("You were attacked by trout. Game over!")
    else:
        print("Please enter a valid response!")
else:
    print("You fell into a hole. Game Over!")
   


