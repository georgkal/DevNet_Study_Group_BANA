import json

with open('JSON.json') as json_file:
    data = json.load(json_file)
    #print(data)
    for spine in data['switches']['spine']:
        print("role: " + spine['role'] + " type: " + spine['type'] + " hostname: " + spine['hostname'])

    for l in data['switches']['leaf']:
        print("role: " + l['role'] + " type: " + l['type'] + " hostname: " + l['hostname'])