#Write your code below this line 👇
def prime_checker(number):
    if number != 2 and number % 2 == 0:
        print("It's not a prime number.")
    elif number != 3 and number % 3 == 0:
        print("It's not a prime number.")
    elif number % 1 == 0 and number % number == 0:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


def prime_checker2(number2):
    is_prime= True
    for i in range (2, number2):
        if number2 % i ==0:
            is_prime=False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

x = int(input("Check this number: "))
prime_checker2(number2=x)