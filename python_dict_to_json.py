# convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4

import json

python_dict = {'English': 78, 'Maths': 88, 'Computers': 100}

print(json.dumps(python_dict, sort_keys = True, indent = 4))