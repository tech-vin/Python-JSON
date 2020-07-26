# convert python obj to json data

import json

python_obj = {
     "Name": "Vineet",
     "profession": "Developer",
     "Country": "India"
     }
print(type(python_obj))    
json_obj = json.dumps(python_obj)

print(python_obj)