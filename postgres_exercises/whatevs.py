d = {'strawberry': 'red', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'super_banana': 'super_yellow', 'pineapple': 'weird', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple', 'pear': 'green', 'aubergine': 'purple'}

for k in d: 
    key_to_compare = k 
    for i in d: 
        if key_to_compare == i:
            del (i)

print(d) 