data = [
    {'name': 'Louis', 'surname': 'Alecu', 'race': 1},
    {'name': 'Louis', 'surname': 'Alecu', 'race': 2},
    {'name': 'Louis', 'surname': 'Alecu', 'race': 3},
    {'name': 'Alyssa', 'surname': 'Cuignet', 'race': 1},
    {'name': 'Alyssa', 'surname': 'Cuignet', 'race': 2},
    {'name': 'Alyssa', 'surname': 'Cuignet', 'race': 3},
    {'name': 'Svetoslav', 'surname': 'Stoilov', 'race': 1},
    {'name': 'Svetoslav', 'surname': 'Stoilov', 'race': 2},
]
# Manipulate the data structure above and reshape it into the data structure below in a new variable called
# drivers
expected_data_structure = [
    {'name': 'Louis', 'surname': 'Alecu'},
    {'name': 'Alyssa', 'surname': 'Cuignet'},
    {'name': 'Svetoslav', 'surname': 'Stoilov'},
]

# Starting code:
drivers = []
for row in data:
    obj = {}
    obj['name'] = row['name']
    obj['surname'] = row['surname']
    print(row)
    if row in drivers:
        break
    


# Proof:
#assert drivers == expected_data_structure


