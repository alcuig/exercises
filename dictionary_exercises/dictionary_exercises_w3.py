""" #1. Write a Python script to sort (ascending and descending) a dictionary by value. 

dictionary = {1:'Hi', 2: 'bye', 5 : 'ff', 9: 'ff', 10: 'ff', 456: 'ff', -1: 'ff'}
for key in sorted (dictionary):
    print(key, dictionary[key])
 """
""" 
"""# 2. Write a Python script to add a key to a dictionary. Go to the editor

""" dictionary = {0: 10, 1: 20}
result = {0: 10, 1: 20, 2: 30}

dictionary[2] = 30
print(dictionary) """

"""

""" 
#3. Write a Python script to concatenate following dictionaries to create a new one. 

#Sample Dictionary :
""" dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
dic4 = {}

for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4) """

"""



4. Write a Python script to check whether a given key already exists in a dictionary. 

""" 
""" fruits = {}
fruits["apple"] = 1
fruits["mango"] = 2
fruits["banana"] = 4

if "apple" in fruits:
    print ('apple is in fruits')
""" """


5. Write a Python program to iterate over dictionaries using for loops. 

""" """ 
fruits = {}
fruits["apple"] = 1
fruits["mango"] = 2
fruits["banana"] = 4

for dict_key, dict_value in fruits.items():
    print(dict_key, '--->', dict_value) """

"""

6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




def list_generator(n):
    dictionary = {}
    for i in range(1, n+1):
        dictionary[i] = i**2
    print(dictionary)

list_generator(1)
list_generator(6)


7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are square of keys. 
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


d = {}
for i in range(1,16):
    d[i]=i*2

print(d)

8. Write a Python script to merge two Python dictionaries. 
""" 
""" 
dic2={3:30, 4:40}
dic3={5:50,6:60}


dic4 = {}
for k in dic2:
    dic4[k] = dic2[k]

for k in dic3:
    dic4[k] = dic3[k]

print(dic4)

"""
""" dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {**dic2, **dic3}
print(dic4) """
""""
9. Write a Python program to iterate over dictionaries using for loops. 
 
dic2={3:30, 4:40}
dic3={5:50,6:60}

def dic_loop(n):
    for k in n:
        print(k, n[k])

dic_loop(dic2) 


10. Write a Python program to sum all the items in a dictionary. 
""" 
""" dic2={3:30, 4:40, 5:50,6:60}

def dic_sum(d):
    sum = 0
    for k in d:
        sum = sum + d[k]
    print(sum)

dic_sum (dic2) """
"""


11. Write a Python program to multiply all the items in a dictionary. 

dic2={3:30, 4:40, 5:50,6:60}

def dic_multiply (d):
    sum = 1
    for k in d: 
        sum = sum *k
    print(sum)

dic_multiply(dic2)    


12. Write a Python program to remove a key from a dictionary.


dic2={3:30, 4:40, 5:50,6:60}

del dic2[6]
print(dic2) 


13. Write a Python program to map two lists into a dictionary. 

# Creates a dict from two lists.
<dict> = dict(zip(keys, values))


ls1 = ['green', 'blue', 'red', 'orange']
ls2= ['snake', 'whale', 'ladybird', 'orangutan']

d = dict(zip(ls1, ls2))
print(d) 


14. Write a Python program to sort a given dictionary by key. 

d_animals = {'green': 'snake', 'blue': 'whale', 'red': 'ladybird', 'orange': 'orangutan'}
for key in sorted(d_animals):
    print(key, d_animals[key]) 
   

15. Write a Python program to get the maximum and minimum value in a dictionary. 
?????

16. Write a Python program to get a dictionary from an object's fields. 
""" 
""" class dObj(object):
    def __init__(self):
        self.strawberry = 'red'
        self.pear = 'green'
        self.aubergine = 'purple'

    def do_nothing(self):
        pass

test = dObj()
print(test.__dict__)
 """
"""

17. Write a Python program to remove duplicates from Dictionary. 

""" 
""" 
d = {'strawberry': 'red', 'pear': 'green', 'aubergine': 'purple', 'snake': 'snakey_colour', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple'}

for k in d: 
    key_to_compare = k 
    for i in d: 
        if key_to_compare == i:
            del (i)

print(d)  

18. Write a Python program to check a dictionary is empty or not. 

d = {'strawberry': 'red', 'pear': 'green', 'aubergine': 'purple', 'snake': 'snakey_colour', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple'}
d_0 = {}

def dic_check(dic):
    if len(dic) == 0:
        print('This dic is empty.')
    else:
        print('There is sth in this dic.')

dic_check(d)
dic_check(d_0)




19. Write a Python program to combine two dictionary adding values for common keys. 

Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


""" 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for k in d1:
    for k2 in d2:
        if k == k2:
            d3[k] = d1[k]+d2[k2]
        else:
            d3[k] = d1[k]
            d3[k2] = d2[k]

print(d3) 
"""



20. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
Click me to see the sample solution

21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
Click me to see the sample solution

22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary. Go to the editor
Click me to see the sample solution

23. Write a Python program to combine values in python list of dictionaries. Go to the editor
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
Click me to see the sample solution

24. Write a Python program to create a dictionary from a string. Go to the editor
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
Click me to see the sample solution

25. Write a Python program to print a dictionary in table format. Go to the editor
Click me to see the sample solution

26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
Expected Output:
6
2
Click me to see the sample solution

27. Write a Python program to convert a list into a nested dictionary of keys. Go to the editor
Click me to see the sample solution

28. Write a Python program to sort a list alphabetically in a dictionary. Go to the editor
Click me to see the sample solution

29. Write a Python program to remove spaces from dictionary keys. Go to the editor
Click me to see the sample solution

30. Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
Click me to see the sample solution

31. Write a Python program to get the key, value and item in a dictionary. Go to the editor
Click me to see the sample solution

32. Write a Python program to print a dictionary line by line. Go to the editor
Click me to see the sample solution

33. Write a Python program to check multiple keys exists in a dictionary. Go to the editor
Click me to see the sample solution

34. Write a Python program to count number of items in a dictionary value that is a list. Go to the editor
Click me to see the sample solution

35. Write a Python program to sort Counter by value. Go to the editor
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
Click me to see the sample solution

36. Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
Click me to see the sample solution

37. Write a Python program to replace dictionary values with their average. Go to the editor
Click me to see the sample solution

38. Write a Python program to match key values in two dictionaries. Go to the editor
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
Click me to see the sample solution

39. Write a Python program to store a given dictionary in a json file. Go to the editor
Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
Click me to see the sample solution

40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary. Go to the editor
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
15
25
35
x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
Click me to see the sample solution

41. Write a Python program to drop empty Items from a given Dictionary. Go to the editor
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}
Click me to see the sample solution

42. Write a Python program to filter a dictionary based on values. Go to the editor
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
Click me to see the sample solution

43. Write a Python program to convert more than one list to nested dictionary. Go to the editor
Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
Click me to see the sample solution

44. Write a Python program to filter the height and width of students, which are stored in a dictionary. Go to the editor
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}
Click me to see the sample solution

45. Write a Python program to check all values are same in a dictionary. Go to the editor
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False
Click me to see the sample solution

46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Go to the editor
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
Click me to see the sample solution

47. Write a Python program to split a given dictionary of lists into list of dictionaries. Go to the editor
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
Click me to see the sample solution

48. Write a Python program to remove a specified dictionary from a given list. Go to the editor
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Click me to see the sample solution

49. Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
Original list:
[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
String values of a given dictionary, into float types:
[{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
Click me to see the sample solution

50. A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary. Go to the editor
Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}
Click me to see the sample solution

51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary. Go to the editor
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
Click me to see the sample solution

52. Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Science
[92, 94, 88]
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Math
[90, 89, 92]
Click me to see the sample solution

53. Write a Python program to find the length of a given dictionary values. Go to the editor
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Length of dictionary values:
{'red': 3, 'green': 5, 'black': 5, 'white': 5}
Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
Length of dictionary values:
{'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
Click me to see the sample solution

54. Write a Python program to get the depth of a dictionary. Go to the editor
Expected Output:
4
Click me to see the sample solution

55. Write a Python program to access dictionary key's element by index. Go to the editor
Expected Output:
physics
math
chemistry
Click me to see the sample solution

56. Write a Python program to convert a given dictionary into a list of lists. Go to the editor
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
Convert the said dictionary into a list of lists:
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
Click me to see the sample solution

57. Write a Python program to filter even numbers from a given dictionary values. Go to the editor
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}
Click me to see the sample solution

58. Write a Python program to get all combinations of key-value pairs in a given dictionary. Go to the editor
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 3, 5], 'VI': [1, 5]}]
Click me to see the sample solution

59. Write a Python program to find the specified number of maximum values in a given dictionary. Go to the editor
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c']
Click me to see the sample solution

60. Write a Python program to find shortest list of values with the keys in a given dictionary. Go to the editor
Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']
Click me to see the sample solution

61. Write a Python program to count the frequency in a given dictionary. Go to the editor
Original Dictionary:
{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
Count the frequency of the said dictionary:
Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})
Click me to see the sample solution

62. Write a Python program to extract values from a given dictionaries and create a list of lists from those values. Go to the editor
Original Dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
Extract values from the said dictionarie and create a list of lists using those values:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
[[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
[['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]
Click me to see the sample solution

63. Write a Python program to convert a given list of lists to a dictionary. Go to the editor
Original list of lists:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
Convert the said list of lists to a dictionary:
{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
Click me to see the sample solution

64. Write a Python program to create a key-value list pairings in a given dictionary. Go to the editor
Original dictionary:
{1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
A key-value list pairings of the said dictionary:
[{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
Click me to see the sample solution

65. Write a Python program to get the total length of all values of a given dictionary with string values. Go to the editor
Original dictionary:
{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
Total length of all values of the said dictionary with string values:
20
Click me to see the sample solution

66. Write a Python program to check if a specific Key and a value exist in a dictionary. Go to the editor
Original dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
Check if a specific Key and a value exist in the said dictionary:
True
True
True
False
False
False
Click me to see the sample solution

67. Write a Python program to invert a given dictionary with non-unique hashable values. Go to the editor
Sample Output:
{8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}
Click me to see the sample solution

68. Write a Python program to combines two or more dictionaries, creating a list of values for each key. Go to the editor
Sample Output:
Original dictionaries:
{'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
{'x': 300, 'y': 'Red', 'z': 600}
Combined dictionaries, creating a list of values for each key:
{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
Click me to see the sample solution

69. Write a Python program to group the elements of a given list based on the given function. Go to the editor
Sample Output:
Original list & function:
[7, 23, 3.2, 3.3, 8.4] Function name: floor:
Group the elements of the said list based on the given function:
{7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
Original list & function:
['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
Group the elements of the said list based on the given function:
{3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}
Click me to see the sample solution

70. Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value. Go to the editor
Sample Output:
{1: 1, 2: 4, 3: 9, 4: 16}
Click me to see the sample solution

71. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list. Go to the editor
Sample Output:
Russell
2
Click me to see the sample solution

72. Write a Python program to invert a dictionary with unique hashable values. Go to the editor
Sample Output:
{10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
Click me to see the sample solution

73. Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key. Go to the editor
Sample Output:
Original list of dictionaries:
[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
Convert a list of dictionaries into a list of values corresponding to the specified key:
[18, 22, 20, 18]
Click me to see the sample solution

74. Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function for each value. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
Dictionary with the same keys:
{'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}
Click me to see the sample solution

75. Write a Python program to find all keys in the provided dictionary that have the given value. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty']
Click me to see the sample solution

76. Write a Python program to combine two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values. The values of the first list need to be unique and hashable. Go to the editor
Sample Output:
Original lists:
['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5]
Combine the values of the said two lists into a dictionary:
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
Click me to see the sample solution

77. Write a Python program to convert given a dictionary to a list of tuples. Go to the editor
Sample Output:
Original Dictionary:
{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
Convert the said dictionary to a list of tuples:
[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]
Click me to see the sample solution

78. Write a Python program to create a flat list of all the keys in a flat dictionary. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the keys of the said flat dictionary:
['Theodore', 'Roxanne', 'Mathew', 'Betty']
Click me to see the sample solution

79. Write a Python program to create a flat list of all the values in a flat dictionary. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]
Click me to see the sample solution

80. Write a Python program to find the key of the maximum value in a dictionary. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')
Click me to see the sample solution

 """