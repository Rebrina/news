from collections import Counter
import json
#import xml.etree.ElementTree as ET

#tree = ET.parse("files/newsafr.xml")
#titles = []

with open("files/newsafr.json", encoding="utf_8_sig") as datafile:
  js_data = json.load(datafile)

news_content = {}
news_description =''
i = 0

for rss in js_data:
  for channel in js_data:
    for items in js_data:
      while i < len(js_data['rss']['channel']['items']):
        news_content = js_data['rss']['channel']['items'][i]['description']
        news_description = news_description + news_content
        i += 1

a = news_description.split(' ')

a_2 = []
i = 0
while i < len(a):
	if len(a[i]) > 6:
		a_2.append(a[i])
		del a[i]
	else:
		i += 1

counts = Counter(a_2)
print(counts.most_common(10))