from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#users_choice = input(f"What would you like? ({Menu.get_items()})")

#print_report
#when user enters 'report' to the prompt, a report should be shown that shows the current resources values ie Water 100ml 


entry = input("Please enter your request: ")
if entry == 'report':
    CoffeeMaker.report()


#check resources sufficient?
print(entry)
if entry == 'espresso' or 'latte' or 'cappuccino':
    check = Menu.find_drink(entry)
    print(check)
    CoffeeMaker.is_resource_sufficient(entry.name) 

#process coins

#check transaction successful?

#Make coffee