import yaml

with open(r'YAML.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    data = yaml.load(file, Loader=yaml.FullLoader)

    #print(data)
    print("Spine: \n")
    for spine in data['spines']:
        print("role: " + spine['role'] + " type: " + spine['type'] + " hostname: " + spine['hostname'])

    print("Leaf: \n")
    for leaf in data['leafs']:
        print("role: " + leaf['role'] + " type: " + leaf['type'] + " hostname: " + leaf['hostname'])