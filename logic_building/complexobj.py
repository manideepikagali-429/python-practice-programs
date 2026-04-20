import json 
def is_complex_num(obj): 
    if 'complex' in obj: 
        return complex(obj['real'], obj['img']) 
    return obj 
# Example JSON strings 
json_str_with_complex = '{"complex": true, "real": 4, "img": 5}' 
json_str_without_complex = '{"real": 4, "img": 3}' 
# Load JSON strings 
complex_object = json.loads(json_str_with_complex, object_hook=is_complex_num) 
simple_object = json.loads(json_str_without_complex, object_hook=is_complex_num) 
# Check and print results 
print("Complex object:", complex_object) 
print("Without complex object:", simple_object)