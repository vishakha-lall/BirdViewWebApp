#!/usr/bin/python

import cgitb
import cgi
import sys
import json
import io
import mysql.connector #Using connector/python provided by oracle
from mysql.connector import errorcode
from collections import OrderedDict
import urllib

try:
	import mastercontroller
except Exception as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

cgitb.enable()


print ("Content-type: application/json")
print "Access-Control-Allow-Origin: *"
print

#data = sys.stdin.read()
try:
	data = cgi.FieldStorage()
except Exception as e:
	outfile = open("errors.log", "a")
	outfile.write(str(e) + 'asdsas ')
	outfile.close()
	exit(1)
#data = ['query_image']
#data = data['query_image']

outfile = open("errors.log", "a")
outfile.write("new request")
outfile.close()

#lullz = data['File']
ruckus = []

for items in data.keys():
	variable = str(items)
	ruckus.append(data.getvalue(variable))


# outfile = open("errors.log", "a")
# outfile.write(str(data))
# outfile.close()


data = ruckus[0]
# 
# #Reading data

# # print sys.prefix
# # print sys.version


DB_NAME = 'BIRDWATCHDBV1'
DB_PORT = '3306'

try:
	cnx = mysql.connector.connect(user='root',password='toor',host='localhost', port = DB_PORT, database = DB_NAME) #connecting to database
except Exception as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

cursor = cnx.cursor()

try:
	cursor.execute("LOCK TABLES VARS WRITE")
except mysql.connector.Error as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

try:
	cursor.execute("SELECT VAR_VAL AS NEWDB FROM VARS WHERE VAR_ID = '1';")
except mysql.connector.Error as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

for row in cursor:
	val = row[0]

try:
	cursor.execute("UPDATE VARS SET VAR_VAL = '%s' WHERE VAR_ID = '1';" %(val+1,))
except Exception as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

try:
	cursor.execute("UNLOCK TABLES")
except mysql.connector.Error as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

filename = "/home/chitransh/Documents/Projects/birds/serverStorage/%s.jpg" % (val,)

try:
	inputfile = open(filename,"wb")
	inputfile.write(data)
	inputfile.close()
except Exception as e:
	outfile = open("errors.log", "a")
	outfile.write(str(e))
	outfile.close()
	exit(1)

try:
	texts, links, species, locations, image_links = mastercontroller.main(val) #Calling mastercontroller
except Exception as e:
	outfile = open("errors.log", "a")
	outfile.write(str(e) + 'in imageOpener')
	outfile.close()
	exit(1)



#responsedict = {}
#responsedict = OrderedDict()

responsedict = []

for i in range(0,5):
	rowdict = {}
	rowdict = OrderedDict()
	rowdict['species_name'] = species[i]
	rowdict['extracted_text'] = texts[i]
	rowdict['wikipedia_link'] = links[i]
	rowdict['location_info'] = locations[i]
	rowdict['image_links'] = image_links[i]

	responsedict.append(rowdict)

global_response = {}
global_response = OrderedDict()

global_response['result'] = True
global_response['tuples'] = responsedict


print (json.JSONEncoder().encode(global_response))