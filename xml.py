import xml.etree.ElementTree as ET
import re

xml = ET.parse("test.xml")
root = xml.getroot()

tag = root.tag
attr = root.attrib
#print("Root tag name is: ",tag)

for c in root.findall("spine"):

 switch = c.find("switch").text
 print("switch :", switch)
 type = c.find("type").text
 print("type :", type)
 hostname = c.find("hostname").text
 print("hostname :", hostname)


