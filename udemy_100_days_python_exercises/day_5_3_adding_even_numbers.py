# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.



#Write your code below this row 👇

total_even_numbers=0

for number in range (1,101):
    if number %2 ==0:
        total_even_numbers+=number 
print (total_even_numbers)

-----
total_even_numbers2=0

for number in range (0,101,2):
    total_even_numbers2 += number 

print (total_even_numbers2)
        
   