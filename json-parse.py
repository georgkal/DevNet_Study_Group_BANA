import json
from pprint import pprint

json_data= open("JSON.json").read()
doc= json.loads(json_data)
pprint(doc)