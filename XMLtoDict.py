import xmltodict

with open('XML.xml') as d:
    doc = xmltodict.parse(d.read())
    #print(doc)

print("Spine: \n")
for spine in doc['body']['spine']:
    print("role: " + spine['role'] + " type: " + spine['type'] + " hostname: " + spine['hostname'])

print("Leaf: \n")
for leaf in doc['body']['leaf']:
    print("role: " + leaf['role'] + " type: " + leaf['type'] + " hostname: " + leaf['hostname'])