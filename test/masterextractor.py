import io
import urllib2
import json
import time
import masterlocationextractor
import wptools
import requests #do i have to re import it

def main(species_name):
	#species_name = species_name.replace(' ', '%20')
	url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=%s&format=json&srlimit=1"%(species_name,)
	url = url.replace(' ', '%20')
	sphdr = {'User-Agent' : 'Mozilla/5.0'}
	reqobj = urllib2.Request(url, headers = sphdr)

	connection = False

	while connection is False:
		try:
			r = urllib2.urlopen(reqobj).read()##modifications here
			response_dict = json.loads(r)
			page_title = response_dict['query']['search'][0]['title']
			page_id = response_dict['query']['search'][0]['pageid']
		except Exception as err:
			outfile = open("errors.log", "a")
			outfile.write(str(err))
			outfile.write(species_name+" si the species name\n")
			outfile.close()
			time.sleep(1)
		else:
			connection = True

	#page_title = page_title.replace(' ','%20')
	url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=%s"%(page_title,)
	url = url.replace(' ', '%20')
	reqobj = urllib2.Request(url, headers = sphdr)

	connection = False

	while connection is False:
		try:
			r = urllib2.urlopen(reqobj).read()
		except Exception as err:
			outfile = open("errors.log", "a")
			outfile.write(str(err))
			outfile.write(species_name+" si the species name err2\n")
			outfile.close()
			time.sleep(1)
		else:
			connection = True


	response_dict = json.loads(r)
	extracted_text = response_dict['query']['pages'][str(page_id)]['extract']
	page_title_ = page_title
	page_title = page_title.replace(' ','_')
	wikipedia_link = "https://en.wikipedia.org/wiki/"+page_title

	page_wp = wptools.page(page_title_)
	page_wp.get_query()
	page_wp.get_parse()

	images_links = ""

	outfile = open("errors.log", "a")

	try:
		link = page_wp.data['infobox']['image']
		url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Image:%s&prop=imageinfo&iiprop=url&format=json'%link
		r = requests.get(url)
		bqq = json.loads(r.content)
		asr = bqq['query']['pages']['-1']['imageinfo'][0]
		images_links = asr['url']
	except Exception as e:
		pass
	
	
	outfile.close()

	location_extract = ""
	try:
		location_extract = masterlocationextractor.main(page_id)
	except Exception as e:
		location_extract = "Not Found"
		outfile = open("errors.log", "a")
		outfile.write(str(e) + ' in masterextractor \n')
		outfile.close()

	return extracted_text, wikipedia_link, location_extract, images_links
#gives neat json response

# https://www.mediawiki.org/w/api.php?action=parse&summary=Some+%5B%5Blink%5D%5D&prop=