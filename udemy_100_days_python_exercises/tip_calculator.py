#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Example Input 
#Welcome to the tip calculator!
#What was the total bill? $124.56
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7

#Example Output
#Each person should pay: $19.93

#Write your code below this line 👇


print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?" ))
tip_percentage_to_add = int(input("How mmuch tip would you like to give? 10, 12, or 15? "))
number_people_splitting_bill = int(input("How many people to split the bill?" ))

bill_with_tip = total_bill * (1 + (tip_percentage_to_add/100))
bill_per_person_unrounded = bill_with_tip/number_people_splitting_bill

result = round(bill_per_person_unrounded, 2)
message = f"Each person should pay: ${result}"
print(message)