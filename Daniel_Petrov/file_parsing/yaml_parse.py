import yaml 
from tabulate import tabulate
from pprint import pprint

with open ('YAML.yaml') as yaml_file:
    yaml_dict = yaml.safe_load(yaml_file)

device_list = []

# Iterate over the dictionary
for device_function in yaml_dict:
    #print(device_funciton) # Check over which key are you iterating 
    for device_id in yaml_dict[device_function]:
        #print (device_id) # Check over which key are you iterating
        device_list.append([device_function,device_id['hostname'],device_id['type']])

# Print a table of content from the file
print (tabulate(device_list, headers=['function','hostname','type'],tablefmt="rst"))
