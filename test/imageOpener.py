#!/usr/bin/python

import cgitb
import cgi
import sys
import json
import mysql.connector #Using connector/python provided by oracle
from mysql.connector import errorcode
from collections import OrderedDict

try:
	import mastercontroller
except Exception as err:
	outfile = open("errors.log", "a")
	outfile.write(str(err))
	outfile.close()
	exit(1)

cgitb.enable()


print ("Content-type: application/json")
print
data = sys.stdin.read() 

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
	texts, links, species = mastercontroller.main(val) #Calling mastercontroller
except Exception as e:
	outfile = open("errors.log", "a")
	outfile.write(str(e))
	outfile.close()
	exit(1)



responsedict = {}
responsedict = OrderedDict()

for i in range(0,5):
	rowdict = {}
	rowdict = OrderedDict()
	rowdict['species_name'] = species[i]
	rowdict['extracted_text'] = texts[i]
	rowdict['wikipedia_link'] = links[i]
	responsedict[i] = rowdict

global_response = {}
global_response = OrderedDict()

global_response['result'] = True
global_response['tuples'] = responsedict
print (json.JSONEncoder().encode(global_response))