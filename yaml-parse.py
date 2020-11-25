import yaml
from pprint import pprint

yaml_data= open("YAML.yaml").read()
doc= yaml.safe_load(yaml_data)
pprint(doc)  
