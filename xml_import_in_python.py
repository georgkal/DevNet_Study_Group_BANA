#!/usr/bin/env python3
#Added by Ivaylo Petrov

import xmltodict
from pprint import pprint

xml_data = open("switches.xml").read()
doc = xmltodict.parse(xml_data)
pprint(doc)
