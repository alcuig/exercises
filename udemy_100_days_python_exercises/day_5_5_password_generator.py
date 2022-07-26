#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password=""
c1=0
c2=0
c3=0

for letter in letters:
    if c1 < nr_letters:
        password += str(random.choice(letters))
        c1+=1

for symbol in symbols:
    if c2 < nr_symbols:
        password += random.choice(numbers)
        c2+=1

for number in numbers:
    if c3 < nr_numbers:
        password += random.choice(symbols)
        c3+=1

random_password=list(password)
random.shuffle(random_password)
final_password=''.join(random_password)

print(final_password)

#ALTERNATIVE SOLUTION
password2=""
for char in range(1,nr_letters+1):
    password2 += random.choice(letters)

for char in range(1,nr_symbols+1):
    password2 += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password2 += random.choice(numbers)

print(password2)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


