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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

hole =input("You step off your drowning rowboat. Mighty she was, although quickly she sank. You land straight in the only visible rockpool. Unfortunate, I know. \nTo your left is a long stretch of fairly bland beach. To your right : a magnificent cape, draped in swollen mango trees. \nMangoes huh? \n... \nSo juicy. \nYour stomach rumbles enthusiastically. \nWhich way should you go : left or right? \n")
if hole.lower() == "left" or 'l':
    print('Grudgingly, you turn your back to what would have been a welcome snack, and make your way across the beach.')
    swim_or_wait = input ("Soon you come across a stream. It's cutting your path to the other side of the beach. It's deep, and the current seems pretty strong. Swim, or wait for the water to die down?")
    if swim_or_wait.lower == "wait" or 'w':
        print("")
        which_door = input("Which door do you choose: blue, red or yellow?")
        if which_door.lower() == "yellow":
            print("Bravo.a, you find the glorious treasure!")
        elif which_door.lower() == 'red' or 'r':
            print("GAME OVER") 
        elif which_door.lower() == "blue" or 'b':
            print("GAME OVER")
        else:
            print("GAME OVER.")
    else:
        print("GAME OVER")
else:
    print(" \"Righty-ho then!\", you shout. With a bombastic swing of your leg, you swivel right - right into an empty rockpool. \n \"Where did all the water go?\" are sadly your last living thoughts before your skull crushes against the barnacled rocks. \n GAME OVER")

