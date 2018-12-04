from pprint import pprint
from collections import Counter
#from lxml import etree
import xml.etree.ElementTree as ET

news_description =''

tree = ET.parse('files/newsafr.xml', parser=ET.XMLParser(encoding='utf-8'))
titles = []
root = tree.getroot()

# поиск в XML
xml_title = root.find('channel/item/description')
#print(type(xml_title))
print(xml_title.text)
xml_items = root.findall("channel/item")
print(len(xml_items))
for xmli in xml_items:
    news_description = news_description + xmli.find("description").text
#print(news_description)

a = news_description.split(' ')
a = [element.lower() for element in a]

a_2 = []
i = 0
while i < len(a):
	if len(a[i]) > 6:
		a_2.append(a[i])
		del a[i]
	else:
		i += 1

counts = Counter(a_2)
pprint(counts.most_common(10))