import sys
import json
import yaml 
from tabulate import tabulate

def json_to_dict (json_file):
    with open (json_file) as file:
        file_dict = json.load(file)
    return file_dict

def yaml_to_dict (yaml_file):
    with open (yaml_file) as file:
        file_dict = yaml.safe_load(file)
    return file_dict

def get_file_extension(file):
    _list = file.split(".")
    lenght = len(_list)
    extension = _list[lenght - 1]
    return extension

working_file = sys.argv[1]
extension = get_file_extension(working_file)

if extension == "json":
    print ("It's JSON, dude !!!")
    ourdict = json_to_dict(working_file)
elif extension == "yaml":
    print ("Welp, it's YAML stupid !!!")
    ourdict = yaml_to_dict(working_file)

device_list = []
# Iterate over the dictionary
for key in ourdict:
    #print(device_funciton) # Check over which key are you iterating 
    for key_ in ourdict[key]:
        #print (device_id) # Check over which key are you iterating
        device_list.append([key,key_['hostname'],key_['type']])
    device_list.append("")

# Print a table of content from the file
print (tabulate(device_list, headers=['function','hostname','type'],tablefmt="rst"))
