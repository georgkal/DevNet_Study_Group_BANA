import json
from pprint import pprint

jason_data = open("jason").read()
doc = json.loads(jason_data)
pprint(doc)