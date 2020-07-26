# convert json data to python object
import json

json_obj = '{"Name": "Vineet", "Profile": "Developer", "Country": "India"}'
python_obj = json.loads(json_obj)
print(json_obj)

print('Name: ',python_obj["Name"])
print('Profile: ',python_obj["Profile"])
print('Country: ', python_obj["Country"])

