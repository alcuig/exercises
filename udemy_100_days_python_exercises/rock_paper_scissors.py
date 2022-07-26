rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_seed=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_seed == 0:
   print (rock)
elif user_seed == 1:
   print (paper)
else:
   print (scissors) 

random.seed(user_seed)
com_choice = random.randint(0,3)


print("Computer chose: ")

if com_choice == 0:
   print (rock)
elif com_choice == 1:
   print (paper)
else:
   print (scissors) 

if com_choice > user_seed:
    if user_seed ==0 and com_choice == 2:
        print("You win")
    print ("You lose")
    

elif user_seed > com_choice:
    if com_choice == 0 and user_seed == 2: 
        print ("You lose")
    else: 
        print("You win")


    
if com_choice == user_seed:
    print("Draw")

