from pprint import pprint
import json
#import xml.etree.ElementTree as ET

#tree = ET.parse("files/newsafr.xml")
#titles = []

with open("files/newsafr.json", encoding="utf_8_sig") as datafile:
  js_data = json.load(datafile)
print(js_data)