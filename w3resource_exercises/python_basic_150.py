""" #2. Write a Python program to get the Python version you are using. Go to the editor

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#3. Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2014-07-05 14:34:14

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S") """

#4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504

import math
from re import A
from unicodedata import name  

""" def area_calc():
    radius = float(input("Please enter the radius of the circle: "))
    area = math.pi * radius **2
    print(area)
    

area_calc() """

#5. Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them. 

""" def reverso ():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    print(last_name + " " + first_name)

reverso() """


#6. Write a Python program which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers. 
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

""" def list_tuple_creator():
    csv_sequence = [input("Please input a sequence of numbers separated by commas: ")]
    lst = csv_sequence.split(",") #this separates the numbers into separate values
    tuple = tuple(lst) #this 'tuple' function creates a tuple out of the values input in parameter 
    print(f"List : {lst}")
    print(f"Tuple : {tuple}")

list_tuple_creator() """

#7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
#Sample filename : abc.java
#Output : java
""" def find_extension ():
    filename=input("What is your file name? ")
    ext = filename.split(".") #separates values around full stop character, creates list
    print(ext[-1]) #prints last value in list which is guaranteed to be extension name

find_extension()
 """


#8. Write a Python program to display the first and last colors from the following list. 
#color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# def f_l_colours(lst):
#     print(lst[0], lst[-1])
    
# f_l_colours(color_list)
""" 
""" """ 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014 ""
 """
""" 
def exam_schedule(exam_start_date):
    print(f"The examination will start from: {exam_start_date[0]} / {exam_start_date[1]} / {exam_start_date[2]}")

exam_st_date = (11, 12, 2014)
exam_schedule(exam_st_date)  """


""" """ """10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5
Expected Result : 615 """
""" 
def add(n):
    n2 = int(str(n) + str(n))
    n3 = int((str(n) + str(n)+ str(n)))
    result= n+int2+int3
    print(result)

add(5) 

"""
"""

""" """ 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
 """
""" def doc_str(x):
    print(x.__doc__)

doc_str(abs)
doc_str(bin) """


"""" "" 12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
""" 
""" 
def cal():
    import calendar #imports python calendar module
    yy = int(input("Give me a year: "))
    mm = int(input("Give me a month number: "))

    #display calendar of input month and year
    print(calendar.month(yy, mm))

cal() """
"""
 """
""" 

 """
""" 
13. Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

""" 
#a heredoc is a is a way of specifying a text block, 
#preserving the line breaks, indentation and other whitespace within the text
#to create a heredoc in python, use triple quotes 
""" """ 
#print("""
#a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example
""")
""" """
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

#python datetime.date(year, month, day) :
#The function returns date object with same year, month and day. All arguments are required.

""" from datetime import date 

numdays = date2-day1
print(numdays.days)

    print(f"{numdays} days")

daysbetween() """
"""

15. Write a Python program to get the volume of a sphere with radius 6.

""" 
""" import math 
def vol_sphere():
    radius = float(input("Enter radius: "))
    vol = 4 / 3 * math.pi * radius** 3
    print(vol) 

vol_sphere() """
"""

16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference. 

""" 
""" def difference():
    num1 = int(input("Enter your number: "))

    #finds absolute difference (ie number without plus or minus sign)
    abs_difference = abs(num1-17)

    if num1 > 17: 
        print(abs_difference * 2) 
    else : 
        print(abs_difference)

difference()  """

"""

17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 


def test_num():
    number = int(input("Input a number: "))
    
    #use range function
    if number in range(900, 1100):
        print("This number is within 100 of 1000.")
    if number in range (1900, 2100):
        print("This number is within 100 of 2000.")
    else: 
        print("This number doesn't fall within 100 of 1000 or 2000.")

test_num()


18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum. 
 
def three_sum():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))
    
    if num1 == num2 and num2 == num3:
        print((num1*3)*3)
    
    else: 
        print(num1 + num2 + num3)

three_sum()    
"""
""" 
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
""" """ If the given string already begins with "Is" then return the string unchanged.  """
""" 
def begins_with_Is():
    str = input("What is your string? ")
    print(str[0:2])

    if "Is" in str[0:2]:
        print(str)
    else:
        print("Is "+str)

begins_with_Is() """ "" """"


20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

"""
""" def copy_me():
    string = input(("What is your string? ")) 
    num_copies = int(input("How many times do you want me to copy your sentence? "))
    new_string = ""
    for i in range(num_copies):
        new_string += string + " "
    
    print(new_string)

copy_me()

21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user.

""" 
""" def even_odd():
    num = int(input("Enter number please: "))
    if num % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")

even_odd()
 """
"""
22. Write a Python program to count the number 4 in a given list. 

""" 
""" def how_many_fours(list):
    four_counter = 0
    for number in list:
        if number == 4:
            four_counter +=1
    
    print(f"There are {four_counter} fours in your list.") 

how_many_fours([1, 2, 3, 3, 3])

how_many_fours([4, 4, 4, 4]) """

"""


23. Write a Python program to get the n (non-negative integer) copies 
of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2. 

""" 
""" def copy_first_two():
    string = input("Give me a string : ")
    new_string = ""
    n = int(input("How many times do you want me to copy your string? "))

    if n <2:
        print(string)

    else:
        for i in range(n):
            new_string += string[0:2] + " " #will add first two characters of string to new_string list with space in between
        print(new_string) #prints list above
            #print(string[0:2])#prints string on different lines


copy_first_two()  """
"""

24. Write a Python program to test whether a passed letter is a vowel or not. 

""" 
""" def is_vowel():
    vowel = input("Please enter a letter : ")
    vowels = ["a", "e", "i", "o", "u"]
    if vowel in vowels: 
        print("This letter is a vowel.")
    else:
        print("This is not a vowel.")

is_vowel()  """

"""

25. Write a Python program to check whether a specified value is contained in a group of values. 

Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

""" 
""" def are_you_here():
    lst_nums = [1, 5, 8, 3]
    find = int(input("Please input the number you are looking for: "))
    print(find in lst_nums) 

are_you_here() """
"""

26. Write a Python program to create a histogram from a given list of integers. 

""" """ 
def histogrammer():
    numbers = input("Please input a list of integers: ")
    lst_numbers = numbers.split()
    print(lst_numbers)
    for string_number in lst_numbers:
        print(string_number)
        print("@" * int(string_number))

histogrammer()  """
"""

27. Write a Python program to concatenate all elements in a list into a string and return it. 
""" 
""" def lst_to_string():
    lst = [1, 2, 3, "my dog", "disconnected", "$"]
    string = ""
    for i in lst:
        string += str(i)
    return string

print(lst_to_string())  """
"""

28. Write a Python program to print all even numbers from a given numbers list 
in the same order and stop the printing if any numbers that come after 237 in the sequence. 

Sample numbers list :

""" 
""" numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def printing_even():
    even_nums = []
    for number in numbers:
        if number == 237:
            even_nums.append(number)
            break
        if number % 2 == 0 :
            even_nums.append(number)
    print(even_nums)

printing_even() 

"""
"""
            

    
29. Write a Python program to print out a set containing 
all the colors from color_list_1 which are not present in color_list_2. 

Test Data :
""" 
""" ##REDO 
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def colours_not_in_list_2():
    uniques= set()
    for colour in color_list_1:
        if colour not in color_list_2:
            uniques += colour

    print (uniques)

colours_not_in_list_2() """
"""
Expected Output :
{'Black', 'White'}




30. Write a Python program that will accept the base and height of a triangle and compute the area. 

""" 
""" def what_is_area():
    base = float(input("Please input the base of the triangle: "))
    height = float (input("Please input the height of the triangle: "))

    area = base * height / 2 

    print(f"The area of your triangle is {area}.")

what_is_area()  """

"""

31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor
Click me to see the sample solution

32. Write a Python program to get the least common multiple (LCM) of two positive integers. Go to the editor
Click me to see the sample solution

33. Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero. 
"""
""" def sum_three():
    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))
    num3 = int(input ("What is your third number: "))

    if num1 == num2 or num2 == num3 or num3 == num1:
        return ("Sum of 0")
    else:
        summed = num1+num2+num3
        return summed 

print(sum_three())  """
"""

34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20. 

""" 
""" def two_summed():
    num1 = int(input("First number please: "))
    num2 = int(input("Second number please: "))

    summed = num1 + num2

    if summed in range(15, 20):
        return 20

    else: 
        return summed

print(two_summed()) """

"""

35. Write a Python program that will return true if 
the two given integer values are equal or their sum or difference is 5. 

""" 
""" def check_5():
    value1 = int(input("First value please: "))
    value2= int(input("Second value please: "))

    if value1 == value2 or ((abs(value1 - value2) == 5)):
        return True 

    else:
        return False

print(check_5()) """

"""

36. Write a Python program to add two objects if both objects are an integer type. 

""" 
""" def add_only_ints(object1, object2):

    if type(object1) == int and type(object2) == int:
        return(object1 + object2)
    else:
        return("These are not integers.")

print(add_only_ints("hello", 2))
print(add_only_ints(4, 2)) """
"""

37. Write a Python program to display your details like name, age, address in three different lines. 

""" 
""" def display_contacts():
    name = input("What is your name? ")
    age = input ("How old are you? ")
    address = input("Where do you live? ")

    print(name)
    print(age)
    print(address)

    print (f"{name}\n{age}\n{address}") #need to use string / quote marks for \n to work 

    print(f""" 
#{name}#will add spaces if don't print at extreme left edge of page
#{age}
#{address}
    #""")

#display_contacts()
"""
"""
""" 
38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
 """

""" def multiplying_sums():
    x = int(input("What is x? "))
    y = int(input("What is y? "))

    multiplied = (x+y)**2
    return(multiplied)

print(multiplying_sums())
 """


""" 39. Write a Python program to compute the future value of a specified principal amount, 
rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79

"""
""" def i_am_your_bank():
    principal = int(input("How much money do you want to borrow? "))
    interest_rate = float(input("What interest rate has your bank given you? "))
    years = int(input("How long will it take for you to pay back your loan? "))

    for year in range(years):
        principal = principal + ((principal / 100) * 3.5)
    
    print(principal) #decimal places?


i_am_your_bank() """

#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 

""" def calc_distance():
    loc1 = input("Input first point in x,y format: ")
    loc2 = input("Input second point in x,y format: ")

    loc1 = loc1.split(",") #splits the string into string numbers
    loc2 = loc2.split(",")

    for i in range(2):
        loc1[i] = int(loc1[i]) #replaces string type numbers in lists with int versions 
        loc2[i] = int(loc2[i])
    
        
    distance = abs(loc1[0] - loc2[0]), abs(loc1[1] - loc2[1]) #if don't put list square brackets, automatically prints as tuple

    print(f"The distance between your two points is {distance}.")

calc_distance()




calc_distance() """


#41. Write a Python program to check whether a file exists. 
#???????


#42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
#????

#43. Write a Python program to get OS name, platform and release information.
#????

#44. Write a Python program to locate Python site-packages. 
#????

#45. Write a Python program to call an external command.
#????

#46. Write a python program to get the path and name of the file that is currently executing.
#????

#47. Write a Python program to find out the number of CPUs using. 
#???

#48. Write a Python program to parse a string to Float or Integer. 
""" def string_transformer():
    string = input("Insert a number : ")
    if "." or "," in string: #checks if number is a decimal
        string = float(string)
    else:
        int(string)
    
    print(type(string))
    print(string + 1)
    return string
    

print(string_transformer()) """



#49. Write a Python program to list all files in a directory in Python. 
#???
""" 
50. Write a Python program to print without newline or space. 
#??

51. Write a Python program to determine profiling of Python programs. 
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
#????

52. Write a Python program to print to stderr. 
#???

53. Write a python program to access environment variables.
#????

54. Write a Python program to get the current username. 
#????

55. Write a Python to find local IP addresses using Python's stdlib.
#???

56. Write a Python program to get height and width of the console window. 
#????

57. Write a Python program to get execution time for a Python method. 
#????

58. Write a Python program to sum of the first n positive integers. 

""" 
""" def sum_n_positives():
    n = int(input("Input the number of positive integers you want summed: "))
    total_positives = 0 
    for number in range(n+1):
        total_positives += number 
    
    return(total_positives)

print(sum_n_positives())  """
#??
"""

59. Write a Python program to convert height (in feet and inches) to centimeters. 

#???

60. Write a Python program to calculate the hypotenuse of a right angled triangle. 
#???

61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. #??

62. Write a Python program to convert all units of time into seconds. 
#??

""" 
""" def to_seconds():
    time = input("Input a period of time: ") #assumed in format X hours or X minutes or X seconds
    if "minute" in time: 
        minutes = int(time[0:2])
        seconds = minutes * 60 
        print(seconds)
    
    if "hour" in time: 
        hours = int(time[0:2])
        seconds = hours * 60 ** 2 
        print(seconds) 

to_seconds()   """
#?? what to do if hours and minutes input 
# what to do if day input

""" def to_seconds_2():
    time = input("Input a period of time: ") #assumed in format XX:XX:XX
    print(time)

    seconds = int(time[-2:])
    print(seconds)

    minutes = int(time[3:5])
    minutes_in_seconds = minutes * 60
    print(minutes_in_seconds)
    print(minutes)

    hours = int(time[:2])
    hours_in_seconds = hours * 60**2
    print(hours)
    print(hours_in_seconds)

    total_seconds = hours_in_seconds + minutes_in_seconds + seconds

    message = f"Your hours in seconds is {hours_in_seconds}. \nYour minutes in seconds is {minutes_in_seconds}. \nCombined with your seconds, this gives you a total of {total_seconds} seconds."
    print(message)

to_seconds_2() """
    
"""






63. Write a Python program to get an absolute file path. 
#??

64. Write a Python program to get file creation and modification date/times. #??

65. Write a Python program to convert seconds to day, hour, minutes and seconds. 

""" 
def second_converter():
    total_seconds = int(input("Please input the total amount of seconds you want to convert to days, hours, minutes and seconds: "))

    days = total_seconds // (24* 3600)
    total_seconds = total_seconds - (days * (24* 3600))
    hours = total_seconds // 3600
    total_seconds = total_seconds - (hours * 3600)
    minutes = total_seconds // 60
    total_seconds = total_seconds - (minutes * 60)
    seconds = total_seconds

    print(f"Days : {days}\nHours : {hours}\nMinutes : {minutes}"\nSeconds : {seconds}")

second_converter()
    """




66. Write a Python program to calculate body mass index. Go to the editor
Click me to see the sample solution

67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. Go to the editor
Click me to see the sample solution

68. Write a Python program to calculate sum of digits of a number. Go to the editor
Click me to see the sample solution

69. Write a Python program to sort three integers without using conditional statements and loops. Go to the editor
Click me to see the sample solution

70. Write a Python program to sort files by date. Go to the editor
Click me to see the sample solution

71. Write a Python program to get a directory listing, sorted by creation date. Go to the editor
Click me to see the sample solution

72. Write a Python program to get the details of math module. Go to the editor
Click me to see the sample solution

73. Write a Python program to calculate midpoints of a line. Go to the editor
Click me to see the sample solution

74. Write a Python program to hash a word. Go to the editor
Click me to see the sample solution

75. Write a Python program to get the copyright information and write Copyright information in Python code. Go to the editor
Click me to see the sample solution

76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. Go to the editor
Click me to see the sample solution

77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. Go to the editor
Click me to see the sample solution

78. Write a Python program to find the available built-in modules. Go to the editor
Click me to see the sample solution

79. Write a Python program to get the size of an object in bytes. Go to the editor
Click me to see the sample solution

80. Write a Python program to get the current value of the recursion limit. Go to the editor
Click me to see the sample solution

81. Write a Python program to concatenate N strings. Go to the editor
Click me to see the sample solution

82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary). Go to the editor
Click me to see the sample solution

83. Write a Python program to test whether all numbers of a list is greater than a certain number. Go to the editor
Click me to see the sample solution

84. Write a Python program to count the number occurrence of a specific character in a string. Go to the editor
Click me to see the sample solution

85. Write a Python program to check whether a file path is a file or a directory. Go to the editor
Click me to see the sample solution

86. Write a Python program to get the ASCII value of a character. Go to the editor
Click me to see the sample solution

87. Write a Python program to get the size of a file. Go to the editor
Click me to see the sample solution

88. Given variables x=30 and y=20, write a Python program to print "30+20=50". Go to the editor
Click me to see the sample solution

89. Write a Python program to perform an action if a condition is true. Go to the editor
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
Click me to see the sample solution

90. Write a Python program to create a copy of its own source code. Go to the editor
Click me to see the sample solution

91. Write a Python program to swap two variables. Go to the editor
Click me to see the sample solution

92. Write a Python program to define a string containing special characters in various forms. Go to the editor
Click me to see the sample solution

93. Write a Python program to get the Identity, Type, and Value of an object. Go to the editor
Click me to see the sample solution

94. Write a Python program to convert a byte string to a list of integers. Go to the editor
Click me to see the sample solution

95. Write a Python program to check whether a string is numeric. Go to the editor
Click me to see the sample solution

96. Write a Python program to print the current call stack. Go to the editor
Click me to see the sample solution

97. Write a Python program to list the special variables used within the language. Go to the editor
Click me to see the sample solution

98. Write a Python program to get the system time. Go to the editor

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
Click me to see the sample solution

99. Write a Python program to clear the screen or terminal. Go to the editor
Click me to see the sample solution

100. Write a Python program to get the name of the host on which the routine is running. Go to the editor
Click me to see the sample solution

101. Write a Python program to access and print a URL's content to the console. Go to the editor
Click me to see the sample solution

102. Write a Python program to get system command output. Go to the editor
Click me to see the sample solution

103. Write a Python program to extract the filename from a given path. Go to the editor
Click me to see the sample solution

104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Go to the editor
Note: Availability: Unix.
Click me to see the sample solution

105. Write a Python program to get the users environment. Go to the editor
Click me to see the sample solution

106. Write a Python program to divide a path on the extension separator. Go to the editor
Click me to see the sample solution

107. Write a Python program to retrieve file properties. Go to the editor
Click me to see the sample solution

108. Write a Python program to find path refers to a file or directory when you encounter a path name. Go to the editor
Click me to see the sample solution

109. Write a Python program to check if a number is positive, negative or zero. Go to the editor
Click me to see the sample solution

110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. Go to the editor
Click me to see the sample solution

111. Write a Python program to make file lists from current directory using a wildcard. Go to the editor
Click me to see the sample solution

112. Write a Python program to remove the first item from a specified list. Go to the editor
Click me to see the sample solution

113. Write a Python program to input a number, if it is not a number generates an error message. Go to the editor
Click me to see the sample solution

114. Write a Python program to filter the positive numbers from a list. Go to the editor
Click me to see the sample solution

115. Write a Python program to compute the product of a list of integers (without using for loop). Go to the editor
Click me to see the sample solution

116. Write a Python program to print Unicode characters. Go to the editor
Click me to see the sample solution

117. Write a Python program to prove that two string variables of same value point same memory location. Go to the editor
Click me to see the sample solution

118. Write a Python program to create a bytearray from a list. Go to the editor
Click me to see the sample solution

119. Write a Python program to round a floating-point number to specified number decimal places. Go to the editor
Click me to see the sample solution

120. Write a Python program to format a specified string limiting the length of a string. Go to the editor
Click me to see the sample solution

121. Write a Python program to determine whether variable is defined or not. Go to the editor
Click me to see the sample solution

122. Write a Python program to empty a variable without destroying it. Go to the editor

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}

Click me to see the sample solution

123. Write a Python program to determine the largest and smallest integers, longs, floats. Go to the editor
Click me to see the sample solution

124. Write a Python program to check whether multiple variables have the same value. Go to the editor
Click me to see the sample solution

125. Write a Python program to sum of all counts in a collections.Go to the editor
Click me to see the sample solution

126. Write a Python program to get the actual module object for a given object. Go to the editor
Click me to see the sample solution

127. Write a Python program to check whether an integer fits in 64 bits. Go to the editor
Click me to see the sample solution

128. Write a Python program to check whether lowercase letters exist in a string. Go to the editor
Click me to see the sample solution

129. Write a Python program to add leading zeroes to a string. Go to the editor
Click me to see the sample solution

130. Write a Python program to use double quotes to display strings. Go to the editor
Click me to see the sample solution

131. Write a Python program to split a variable length string into variables. Go to the editor
Click me to see the sample solution

132. Write a Python program to list home directory without absolute path. Go to the editor
Click me to see the sample solution

133. Write a Python program to calculate the time runs (difference between start and current time) of a program. Go to the editor
Click me to see the sample solution

134. Write a Python program to input two integers in a single line. Go to the editor
Click me to see the sample solution

135. Write a Python program to print a variable without spaces between values. Go to the editor
Sample value : x =30
Expected output : Value of x is "30"
Click me to see the sample solution

136. Write a Python program to find files and skip directories of a given directory. Go to the editor
Click me to see the sample solution

137. Write a Python program to extract single key-value pair of a dictionary in variables. Go to the editor
Click me to see the sample solution

138. Write a Python program to convert true to 1 and false to 0. Go to the editor
Click me to see the sample solution

139. Write a Python program to valid a IP address. Go to the editor
Click me to see the sample solution

140. Write a Python program to convert an integer to binary keep leading zeros. Go to the editor
Sample data : x=12
Expected output : 00001100
0000001100
Click me to see the sample solution

141. Write a python program to convert decimal to hexadecimal. Go to the editor
Sample decimal number: 30, 4
Expected output: 1e, 04
Click me to see the sample solution

142. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False. Go to the editor
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Click me to see the sample solution

143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. Go to the editor
Click me to see the sample solution

144. Write a Python program to check whether variable is integer or string. Go to the editor
Click me to see the sample solution

145. Write a Python program to test if a variable is a list or tuple or a set. Go to the editor
Click me to see the sample solution

146. Write a Python program to find the location of Python module sources. Go to the editor
Click me to see the sample solution

147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. Go to the editor
Click me to see the sample solution

148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Go to the editor
Note: Do not use built-in functions.
Click me to see the sample solution

149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. Go to the editor
Click me to see the sample solution

150. Write a Python function to check whether a distinct pair of numbers whose product is odd present in a sequence of integer values. Go to the editor
Click me to see the sample solution """