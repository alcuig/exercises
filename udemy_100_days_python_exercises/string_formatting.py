# Amend the code below to produce the following message using a "formatted string literal" Colour Selection: Blue, Green

# Colours = ['Red','Blue','Green','Purple']
# Selection = ___________
# print(Selection)

Colours = ['Red','Blue','Green','Purple']
Selection = f"Colour Selection : {Colours[1]}, {Colours[2]}"
print(Selection)

# """ Amend the code below to print "LeafBlue" using the format function

# Types = ['Leaf', 'Fire', 'Water']
# Colours = ['Green', 'Red', 'Blue']
# Version1 = ___________
# print(Version1) """

Types = ['Leaf', 'Fire', 'Water']
Colours = ['Green', 'Red', 'Blue']
Version1 = "{}{}".format(Types[0],Colours[2])
print(Version1)s