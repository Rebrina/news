from pprint import pprint
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
        print(i)

a = news_description.split(' ')

print(a)

def sortByLength(inputStr):
        return len(inputStr)

a.sort(key=sortByLength, reverse=True)

for i in range(0,10):
  print(a[i])