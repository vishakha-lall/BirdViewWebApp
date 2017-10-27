import requests
import mwparserfromhell as mw
import wptools
import re
import json
from bs4 import BeautifulSoup as BS

def main(page_id):
	url = "https://en.wikipedia.org/w/api.php?action=parse&pageid=%s&prop=text&format=json" % page_id
	r = requests.get(url)
	decoded_r = json.loads(r.content)
	raw_code = decoded_r['parse']['text']['*']
	soup = BS(raw_code)
	g_data = soup.find_all('h2')
	dist_tag = None
	for items in g_data:
		if('distribution' in items.text.lower()):
			dist_tag = items

	if(dist_tag is None):
		return "Not found"

	f_data = dist_tag.find('a')
	href_str = f_data['href']
	section_index = href_str.find("section")
	section_id = href_str[section_index+8]

	url = "https://en.wikipedia.org/w/api.php?action=parse&section=%s&pageid=%s&prop=text&format=json" % (section_id, page_id)
	r = requests.get(url)
	try:
		decoded_r = json.loads(r.content)
		raw_code = decoded_r['parse']['text']['*']
		wikicode = mw.parse(raw_code)
		plaintext = wikicode.strip_code()
		plaintext = plaintext.lower()
		plaintext = plaintext.replace('\n', ' ')
		#plaintext = plaintext.replace('\\', ' ')
		plaintext = plaintext.replace(u'\xa0', ' ')
		plaintext = plaintext.replace(u'\xe1', ' ')
		plaintext = re.sub(' +',' ',plaintext)
		plaintext = re.sub('\[+\d+\[', '', plaintext)
		plaintext = plaintext.replace('[edit]', '')
		seperator = " ^ Cite error"
		plaintext = plaintext.split(seperator, 1)[0]
	except Exception as e:
		outfile = open("errors.log", "a")
		outfile.write(str(e) + ' in masterlocationextractor \n')
		outfile.close()
	return plaintext
	#get raw code
	#get the h2 tags
	#get the a tag
	#write code for getting section
	#request section
	#parse it
	#use nlp to get places
	

	
