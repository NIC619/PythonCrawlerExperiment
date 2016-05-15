import urllib
import re
from BeautifulSoup import *

url = "https://tw.dictionary.yahoo.com/dictionary?p="
inputs = raw_input("what's the word you are looking for?")

url += inputs
raw_url_data = urllib.urlopen(url).read()

soup = BeautifulSoup(raw_url_data)
##### search for word class, e,g. vi,vt,n,etc. (which are in span tag with class="fz-s mb-10")
word_class_lists = soup.findAll("span", attrs={"class": "fz-s mb-10"})
word_class_list = []

for i in word_class_lists:
	##### extract word class text from span tag
	tmp = re.findall(r'<span[^>]*>(.+)</span>',str(i))[0]
	word_class_list.append(tmp)

##### search for translation(which are in h4 tags)
translation_lists = re.findall(r'<h4[^>]*>([^<]+)</h4>',raw_url_data)  

##### print all translation with number prefix
word_class = 0
for i in translation_lists:
	if re.match('1. ',i):
		print word_class_list[word_class],":"
		word_class += 1
	print "    ",i

