# convert encoded json to python object 
import json

j_obj_dict = '{"English": 90, "Maths": 99, "Social": 56 }'
j_obj_list ='["apple", 10, "milk"]'
j_obj_tuple = '("Sunny", "M", 23)'
j_obj_str = '"Game On"'
j_obj_int = '34'
j_obj_float = '98.54'


python_dict = json.loads(j_obj_dict)
python_list = json.loads(j_obj_list)
#python_tuple = json.loads(j_obj_tuple)
python_str = json.loads(j_obj_str)
python_int = json.loads(j_obj_int)
python_float = json.loads(j_obj_float)


print('Dictonary: ', python_dict)
print('List: ', python_list)
#print('Tuple: ', python_tuple)
print('String: ',python_str)
print('Integer: ', python_int)
print('Float: ', python_float)