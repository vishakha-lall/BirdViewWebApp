import masterlabeller
import masterextractor

def main(object_id):
	image_path = '/home/chitransh/Documents/Projects/birds/serverStorage/'+str(object_id)+'.jpg'
	class_list, species_list = masterlabeller.main(image_path)
	outfile = open("errors.log", "a")
	outfile.write("Labelling completed\n")
	outfile.close()
	extracted_texts = []
	wikipedia_links = []
	locations_texts = []
	image_links_superlist = []
	for items in species_list:
		try:
			extracted_text, wikipedia_link, locations, image_links = masterextractor.main(items)
		except Exception as e:
			extracted_text, wikipedia_link, locations, image_links = ("","","","")
			outfile = open("errors.log", "a")
			outfile.write(str(e) + ' in mastercontroller \n')
			outfile.close()
		#extracted_text, wikipedia_link = masterextractor.main(items)
		extracted_texts.append(extracted_text)
		wikipedia_links.append(wikipedia_link)
		locations_texts.append(locations)
		image_links_superlist.append(image_links)
		
	return extracted_texts, wikipedia_links, species_list, locations_texts, image_links_superlist

def main_2(species_name):
	outfile = open("errors.log", "a")
	outfile.write(species_name + " name coasdadsmpleted\n")
	outfile.close()
	extracted_text, wikipedia_link, locations, image_links = masterextractor.main(species_name)
	return extracted_text, wikipedia_link, locations, image_links