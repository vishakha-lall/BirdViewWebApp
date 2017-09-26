#!/usr/bin/env python

'''
@Author: Chitransh Gaurav
@Organisation: Droom Technology
@Description: Searches OBV database for possible matches of trim or model/trim
@Notes:

Normalization is not a great idea for all the cases. In some cases, it helps though when data set is large
Lower case conversion helps everywhere

TIME COMPLEXITY WORST CASE O(N^4), average O(N^2)

Times:
1000 chars, 1000 times 1.45s
500 chars, 1000 times 0.41s
100 chars, 1000 times 0.15 s
10 chars, 1000 times 0.03

1000 chars, 1 time, order of 10^-3 s

Anomalies : 
(Not from droom database, cartrade)
http://localhost/new5.py?make=Porsche&model=Boxster&year=2008&trim=S%20Tiptronic
http://localhost/new5.py?make=Maruti%20Suzuki&model=Alto&year=2011&trim=LX%20BS%20IV
http://localhost/new5.py?make=Lamborghini&model=Gallardo&year=2013&trim=LP%20550-2%20Ltd%20Edition
http://localhost/new5.py?make=Mitsubishi&model=Cedia&year=2011&trim=New%20Spirit
http://localhost/new5.py?make=Chevrolet&model=Aveo&year=2014&trim=LS%201.4
http://localhost/new5.py?make=Maruti%20Suzuki&model=800&year=2010&trim=AC%20BS%20II

Droom Anomalies:


Not Found:
http://localhost/new5.py?make=hero&model=hunk&year=2016&trim=rear%20drum%20brake
http://localhost/new5.py?make=tvs&model=wego&year=2016&trim=disc
http://localhost/new5.py?make=yamaha&model=alpha&year=2016&trim=ltd.edition
http://localhost/new5.py?make=ducati&model=superbike&year=2017&trim=panigale%20r

Unsure (Maybe correct):
http://localhost/new5.py?make=tata&model=nano&year=2013&trim=genx%20xe
http://localhost/new5.py?make=bajaj&model=discover&year=2016&trim=drum-125cc
http://localhost/new5.py?make=ford&model=figo&year=2016&trim=1.5d%20base%20mt

Correct Matches: (from droom, cartrade)
http://localhost/new5.py?make=Fiat&model=Grande%20Punto&year=2013&trim=Emotion%20Pack%201.4
http://localhost/new5.py?make=Mahindra&model=Bolero&year=2010&trim=2011%20SLE
http://localhost/new5.py?make=Mini&model=Convertible&year=2013&trim=1.6
http://localhost/new5.py?make=Hyundai&model=Accent&year=2010&trim=CNG
http://localhost/new5.py?make=Chevrolet&model=Beat&year=2015&trim=1.0%20LS%20TCDi%20Diesel
http://localhost/new5.py?make=Maruti%20Suzuki&model=800&year=2011&trim=AC%20BS%20II
http://localhost/new5.py?make=Mahindra&model=Reva&year=2015&trim=e2o%20T2
http://localhost/new5.py?make=Mahindra%20Reva&model=e2o&year=2015&trim=T2
http://localhost/new5.py?make=maruti%20suzuki&model=eeco&year=2012&trim=5%20str%20with%20a/c+htr%20cng
http://localhost/new5.py?make=hyundai&model=santa%20fe&year=2016&trim=4wd%20at
http://localhost/new5.py?make=chevrolet&model=tavera%20fe&year=2016&trim=neo%203%20ls-9%20str-bsiii
http://localhost/new5.py?make=toyota&model=fortuner%20fe&year=2016&trim=2.8%204x4%20mt
http://localhost/new5.py?make=hero&model=pleasure&year=2012&trim=100cc
http://localhost/new5.py?make=tvs&model=wego&year=2016&trim=110
http://localhost/new5.py?make=honda&model=city&year=2001&trim=s
http://localhost/new5.py?make=maruti%20suzuki&model=swift%20dzire&year=2015&trim=lxi%201.2%20bs-iv
http://localhost/new5.py?make=ford&model=endeavour&year=2015&trim=2.5l%204x4%20mt
http://localhost/new5.py?make=nissan&model=terrano&year=2015&trim=xv%20d%20thp%20110%20ps
http://localhost/new5.py?make=yamaha&model=ray&year=2014&trim=110cc
http://localhost/new5.py?make=honda&model=amaze&year=2016&trim=1.5%20s%20i-dtec%20opt
http://localhost/new5.py?make=hero&model=achiever&year=2014&trim=150cc
http://localhost/new5.py?make=hero&model=glamour&year=2016&trim=pgm%20fi%20125cc
http://localhost/new5.py?make=suzuki&model=gs%20150%20r&year=2008&trim=150cc
http://localhost/new5.py?make=bajaj&model=avenger&year=2007&trim=180cc
http://localhost/new5.py?make=tvs&model=scooty%20pep%20plus&year=2015&trim=100%20cc
http://localhost/new5.py?make=mahindra&model=duro%20dz&year=2012&trim=125%20cc
http://localhost/new5.py?make=bajaj&model=ct%20100&year=2003&trim=100cc
http://localhost/new5.py?make=hyundai&model=verna&year=2010&trim=vtvt%201.6
http://localhost/new5.py?make=mahindra&model=xylo&year=2009&trim=base
http://localhost/new5.py?make=renault&model=duster&year=2013&trim=110%20ps%20rxl
http://localhost/new5.py?make=royal%20enfield&model=standard&year=1982&trim=350
http://localhost/new5.py?make=hero&model=cd%20deluxe&year=2008&trim=100cc
http://localhost/new5.py?make=maruti%20suzuki&model=ritz&year=2012&trim=vxi
http://localhost/new5.py?make=hyundai&model=grand%20i10&year=2013&trim=magna
http://localhost/new5.py?make=audi&model=q5&year=2014&trim=quattro%20technology%20pack
http://localhost/new5.py?make=bmw&model=x1&year=2010&trim=highline
http://localhost/new5.py?make=ducati&model=monster&year=2013&trim=1200%20s
http://localhost/new5.py?make=tata&model=sumo&year=2006&trim=victa%20cx
http://localhost/new5.py?make=tata&model=sumo&year=2008&trim=victa%20cx
http://localhost/new5.py?make=tata&model=sumo&year=2006&trim=victa%20cx%209%20str
http://localhost/new5.py?make=tata&model=sumo&year=2010&trim=victa%20gx%20tc%208%20str
http://localhost/new5.py?make=hyundai&model=i20&year=2009&trim=asta%201.4%20crdi%206%20speed
http://localhost/new5.py?make=bmw&model=z4&year=2015&trim=xdrive%2030d%20expedition
http://localhost/new5.py?make=austin%20motor&model=a40&year=1953&trim=somerset
http://localhost/new5.py?make=hero&model=hawk&year=2015&trim=27%20inches
http://localhost/new5.py?make=maruti%20suzuki&model=ritz&year=2016&trim=vxi%20bs%20iv

interesting and correct:
http://localhost/new5.py?make=honda&model=cb%20twister&year=2015&trim=110cc
http://localhost/new5.py?make=hero&model=splendor%20plus&year=2006&trim=100cc
http://localhost/new5.py?make=maruti%20suzuki&model=sx4&year=2015&trim=zxi%20(o)%20mt


'''
import cgitb
import cgi
import mysql.connector #Using connector/python provided by oracle
from mysql.connector import errorcode
from fuzzywuzzy import fuzz #uses underlying sequence matcher from Python, pip install fuzzywuzzy, pip install python-levenshtein
import re
import json
from collections import OrderedDict

cgitb.enable()

def stripSpacesHyphensSort(inputString):
	inputString = inputString.replace('-',' ')
	inputString = re.sub(' +',' ', inputString)
	tokens = inputString.split(' ')
	tokens.sort()
	inputString = ""
	for items in tokens:
		inputString += (items)

	return inputString

def concatModelTrimAndMatch():
	global prod_id
	list_models_trims = []

	try:
		cursor.execute("SELECT id,make,model,year,trim AS NEWDB FROM products WHERE make = '%s' AND year = %s;" %(car_details['make'], car_details['year']))
	except mysql.connector.Error as err:
		outfile = open("errors.log", "a")
		outfile.write(str(err))
		outfile.close()
		exit(1)
	for row in cursor:
		temp_row = []
		for items in row:
			temp_row.append(items)
		list_models_trims.append(temp_row)
		# print '<br>'
		# print row

	max_similarity_index = 0
	max_prod_id = -1

	source_string = stripSpacesHyphensSort(car_details['model'].lower()+" "+car_details['trim'].lower())
	# print source_string 
	# print '<br>'
	for items in list_models_trims:
		similarity_index = fuzz.token_sort_ratio(source_string, stripSpacesHyphensSort(items[2].lower()+" "+items[4].lower()))
		if max_similarity_index < similarity_index:
			max_similarity_index = similarity_index
			max_prod_id = items[0]

	if(max_similarity_index > 60):
		prod_id = max_prod_id

	return max_similarity_index

def carMakeNormalizer(car_make):

	car_make = car_make.replace('-',' ')
	car_make = re.sub(' +',' ', car_make)

	tokens_make = car_make.split(' ')
	cap_tokens = []
	#redundant-> not required, might be useful for for saving in plaintext
	for items in tokens_make:
		word_list = list(items)
		if(items.istitle() == False):
			word_list[0] = chr(ord(word_list[0])-32)
		cap_tokens.append("".join(word_list))
		
	car_make = ""	
	car_make+=(cap_tokens[0])

	for items in range(1,len(cap_tokens)):
		car_make += " "+cap_tokens[items]



	if(car_make == 'Mercedes Benz'):
		car_make = car_make.replace(' ','-')

	return car_make

def printTuple(prod_id, similarity_index):
	if prod_id != -1:
		try:
			cursor.execute("SELECT id,make,model,year,trim AS NEWDB FROM products WHERE id = '%s' " %(prod_id,))
		except mysql.connector.Error as err:
			outfile = open("errors.log", "a")
			outfile.write(str(err))
			outfile.close()
			exit(1)
		tupledata = []

		for row in cursor:
			tupledata.append(row)

		responsedict = {}
		responsedict = OrderedDict()

		responsedict['id'] = tupledata[0][0]
		responsedict['make'] = tupledata[0][1]
		responsedict['model'] = tupledata[0][2]
		responsedict['year'] = tupledata[0][3]
		responsedict['trim'] = tupledata[0][4]
		responsedict['similarity_index'] = similarity_index

		data = {}
		data = OrderedDict()

		data['result'] = "Found"
		data['values'] = responsedict

		print (json.JSONEncoder().encode(data))
	else:

		responsedict = {}
		responsedict = OrderedDict()

		responsedict['id'] = -1
		responsedict['make'] = -1
		responsedict['model'] = -1
		responsedict['year'] = -1
		responsedict['trim'] = -1
		responsedict['similarity_index'] = similarity_index

		data = {}
		data = OrderedDict()

		data['result'] = "Not Found"
		data['values'] = responsedict

		print (json.JSONEncoder().encode(data))

#html code
print ("Content-type: application/json")
print 

# print("Content-Type: text/html;charset=utf-8")

# print "Content-type:text/html\r\n\r\n"
# print '<html>'
# print '<head>'
# print '<title>Trim Matcher</title>'
# print '</head>'
# print '<body>'
# print '<h5>Result</h5>'

#html code ends

arguments = cgi.FieldStorage()

car_details = {}#a dictionary to store parameters 'make', 'model', 'year', 'trim' in call
car_details = dict()

# print "inputs:"

for i in arguments.keys():
	# print i, ' ',arguments[i].value
	car_details[i] = arguments[i].value

#Establishing MySql connection

car_details['make'] = carMakeNormalizer(car_details['make'])


DB_PORT = '3306'
cnx = mysql.connector.connect(user='root',password='toor',host='localhost', port = DB_PORT, database='OBV')#These are default settings
cursor = cnx.cursor()

#Obtained cursor

#Searching for Exact match of MMY

try:
	cursor.execute("SELECT id,make,model,year,trim AS NEWDB FROM products WHERE make = '%s' AND model = '%s' AND year = %s;" %(car_details['make'], car_details['model'], car_details['year']))
except mysql.connector.Error as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

#stores list of rows with exact match of MMY
list_trims = []
for row in cursor:
	temp_row = []
	for items in row:
		temp_row.append(items)
	list_trims.append(temp_row)
	# print '<br>'
	# print row

#if returned list is not empty, i.e. MMY Matched
if(len(list_trims) != 0):
	prod_id = -1 

	#Search for exact match of MMYT
	for items in list_trims:
		if(items[4].lower() == car_details['trim'].lower()):
			prod_id = items[0]

	#if exact match not found
	if(prod_id == -1):#If complete match not found
		# print '<br>'
		# print "Complete match for trim not found!"
		# print '<br>'

		#using trim in lower case as source string
		lower_case_trim = car_details['trim'].lower()
		tokens_source = lower_case_trim.split(' ')

		#for maximal match
		maxcnt = 0
		max_prod_id = -1

		#for maximal reverse matching
		maxrevcnt = 0
		max_rev_prod_id = -1
		maxlenitem = -1

		#iterating over the rows
		for items in list_trims:#iterating over list of trims with matched make, model, year
			tokens_dest = items[4].lower().split(' ')
			cnt = 0
			cntrev = 0
			for tokens_source_iter in tokens_source:
				if tokens_source_iter in tokens_dest:
					cnt += 1

			for tokens_dest_iter in tokens_dest:
				if tokens_dest_iter in tokens_source:
					cntrev += 1

			if cnt > maxcnt:
				maxcnt = cnt
				max_prod_id = items[0]

			if cntrev > maxrevcnt:
				maxrevcnt = cnt
				max_rev_prod_id = items[0]
				maxlenitem = len(tokens_dest)

		#calculating percentage match of tokens from source to dest and vice versa
		percentage_match = (maxcnt/len(tokens_source))*100
		percentage_rev_match = (maxrevcnt/maxlenitem)*100
		if(percentage_match > 70):#threshold for word percentage match 70%
			prod_id = max_prod_id

		if(prod_id == -1):#if word percentage did not exceed 70%, use fuzzywuzzy, improved sequence matcher
			lower_case_trim = car_details['trim'].lower()
			max_similarity_index = 0
			#since this is costly, it will be called after maximal matching of tokens is not resulting in anything
			for items in list_trims:
				similarity_index = fuzz.token_sort_ratio(lower_case_trim, items[4].lower())
				if max_similarity_index < similarity_index:
					max_similarity_index = similarity_index
					max_prod_id = items[0]

			prod_id = -1
			concat_similarity_index = concatModelTrimAndMatch()

			concat_prod_id = prod_id

			trim_prod_id = max_prod_id
			trim_similarity_index = max_similarity_index

			if concat_prod_id != -1 or trim_similarity_index > 60:#as per official python documentation, as per the rule of thumb 0.6 index is a good match
				if(trim_similarity_index > concat_similarity_index):
					printTuple(trim_prod_id, trim_similarity_index)
				else:
					printTuple(concat_prod_id, concat_similarity_index)
			elif(percentage_rev_match > 70):
				prod_id = max_rev_prod_id
				printTuple(prod_id, percentage_rev_match)
			else:
				printTuple(-1, 0)
		else:
			printTuple(prod_id, percentage_match)

	else:#Complete Match Found
		printTuple(prod_id,100)
########################################################################################################################################
#If model mismatch#
########################################################################################################################################
else:
	# print '<br>'
	# print 'Model Not Found'
	#if model was not found, simply concatenate and perform fuzzywuzzy matching
	list_models_trims = []
	try:
		cursor.execute("SELECT id,make,model,year,trim AS NEWDB FROM products WHERE make = '%s' AND year = %s;" %(car_details['make'], car_details['year']))
	except mysql.connector.Error as err:
		outfile = open("errors.log", "a")
		outfile.write(str(err))
		outfile.close()
		exit(1)
	for row in cursor:
		temp_row = []
		for items in row:
			temp_row.append(items)
		list_models_trims.append(temp_row)
		# print '<br>'
		# print row

	lower_case_model = car_details['model'].lower().replace('-','').replace(' ','')
	max_similarity_index_model = 0
	model_max = ""

	prod_id = -1
	for items in list_models_trims:
		target_string = items[2].lower().replace('-','').replace(' ','')
		similarity_index = fuzz.token_sort_ratio(lower_case_model, target_string)
		if max_similarity_index_model < similarity_index:
			max_similarity_index_model = similarity_index
			model_max = items[2]
	# print '<br>'
	# print "Similar Model Found ", model_max, " with similarity ", max_similarity_index_model, " %"
	

	if(max_similarity_index_model > 60):
	#-----------------------
		list_trims = []
		for items in list_models_trims:
			if items[2] == model_max:
				list_trims.append(items)
		prod_id = -1 

		#Search for exact match of MMYT
		for items in list_trims:
			if(items[4].lower() == car_details['trim'].lower()):
				prod_id = items[0]

		#if exact match not found
		if(prod_id == -1):#If complete match not found
			# print '<br>'
			# print "Complete match for trim not found!"
			# print '<br>'

			#using trim in lower case as source string
			lower_case_trim = car_details['trim'].lower()
			tokens_source = lower_case_trim.split(' ')

			#for maximal match
			maxcnt = 0
			max_prod_id = -1

			#for maximal reverse matching
			maxrevcnt = 0
			max_rev_prod_id = -1
			maxlenitem = -1

			#iterating over the rows
			for items in list_trims:#iterating over list of trims with matched make, model, year
				tokens_dest = items[4].lower().split(' ')
				cnt = 0
				cntrev = 0
				for tokens_source_iter in tokens_source:
					if tokens_source_iter in tokens_dest:
						cnt += 1

				for tokens_dest_iter in tokens_dest:
					if tokens_dest_iter in tokens_source:
						cntrev += 1

				if cnt > maxcnt:
					maxcnt = cnt
					max_prod_id = items[0]

				if cntrev > maxrevcnt:
					maxrevcnt = cnt
					max_rev_prod_id = items[0]
					maxlenitem = len(tokens_dest)

			#calculating percentage match of tokens from source to dest and vice versa
			percentage_match = (maxcnt/len(tokens_source))*100
			percentage_rev_match = (maxrevcnt/maxlenitem)*100
			if(percentage_match > 70):#threshold for word percentage match 70%
				prod_id = max_prod_id

			if(prod_id == -1):#if word percentage did not exceed 70%, use fuzzywuzzy, improved sequence matcher
				lower_case_trim = car_details['trim'].lower()
				max_similarity_index = 0
				#since this is costly, it will be called after maximal matching of tokens is not resulting in anything
				for items in list_trims:
					similarity_index = fuzz.token_sort_ratio(lower_case_trim, items[4].lower())
					if max_similarity_index < similarity_index:
						max_similarity_index = similarity_index
						max_prod_id = items[0]

				prod_id = -1
				concat_similarity_index = concatModelTrimAndMatch()

				concat_prod_id = prod_id

				trim_prod_id = max_prod_id
				trim_similarity_index = max_similarity_index

				if concat_prod_id != -1 or trim_similarity_index > 60:#as per official python documentation, as per the rule of thumb 0.6 index is a good match
					if(trim_similarity_index > concat_similarity_index):
						printTuple(trim_prod_id, trim_similarity_index)
					else:
						printTuple(concat_prod_id, concat_similarity_index)
				elif(percentage_rev_match > 70):
					prod_id = max_rev_prod_id
					printTuple(prod_id, percentage_rev_match)
				else:
					printTuple(-1,0)
			else:
				printTuple(prod_id,100)

		else:#Complete Match Found
			printTuple(prod_id, 100)

	#	---------------------------------
	else:
		prod_id = -1
		similarity_index = concatModelTrimAndMatch()
		if(prod_id != -1):
			printTuple(prod_id, similarity_index)
		else:
			printTuple(-1, 0)

# print '</body>'
# print '</html>'