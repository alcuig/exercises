# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print('Hello')
    print('Bonjour')
    print('Aloha')

greet()

def greet_with_name(name):
    print(f'Hello {name}!')
    print(f'Bonjour{name}!')
    print(f'Aloha {name}!')

greet_with_name("Jake")

#Functions with more than 1 input: 
def greet_with(name, location):
    print(f"Hello {name}!") 
    print(f"What is it like in {location} right now?")

greet_with("Joanne", "Moscow")

#Calling functions with keyword arguments:
greet_with(location="Macedonia", name="Horatio")
