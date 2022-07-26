# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_combined= name1.lower() + name2.lower()

total1 = names_combined.count("t") + names_combined.count("r") + names_combined.count("u") + names_combined.count("e")
total2 =names_combined.count("l") + names_combined.count("o") + names_combined.count("v") + names_combined.count("e")

score = int(str(total1)+ str(total2))

message= f"Your score is {score}"

if score <= 10 or score >= 90 :
    print (message + ", you go together like coke and mentos.")

elif score >= 40 and score <= 50 :
    print (message + ", you are alright together.")

else:
    print(message + ".")