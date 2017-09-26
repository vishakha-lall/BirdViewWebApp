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
	for items in species_list:
		extracted_text, wikipedia_link = masterextractor.main(items)
		extracted_texts.append(extracted_text)
		wikipedia_links.append(wikipedia_link)
	return extracted_texts, wikipedia_links, species_list
