print('''
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
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
first_question = input("You're at cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if first_question == 'left':
    second_question = input("You came to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_question == 'wait':
        third_question = input('You arrive at the island unharmed. There is a house within 3 doors. One red, One yellow and one blue. Which olour do you choose?\n').lower()
        if third_question == 'red':
            print('Burned by fire.\nGame Over.')
        elif third_question == 'blue':
            print('Eaten by beasts.\nGame Over.')
        elif third_question == 'yellow':
            print('You Win!')
        else:
            print('Game Over!')
    else:
        print('Attacked by trout.\nGame Over.')
else:
    print('Fall into hole.\nGame Over.')

