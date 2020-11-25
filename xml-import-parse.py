import xmltodict
from pprint import pprint

xml_data= open("XML.xml").read()
doc= xmltodict.parse(xml_data)
pprint(doc)