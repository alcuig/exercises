""" fruit = ['Apple', 'Watermelon', 'Grapes', 'Pear', 'Orange']
Write some code to produce a numbered list of fruit using the list above

i.e. the output of the code would be:

1 Apple
2 Watermelon
3 Grapes
4 Pear
5 Orange """

fruit = ['Apple', 'Watermelon', 'Grapes', 'Pear', 'Orange']

for x in enumerate(fruit,1):
    print(x[0], x[1])

print(1, "Alyssa")