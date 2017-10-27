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

arguments = cgi.FieldStorage()

bird_name = {}#a dictionary to store parameters 'make', 'model', 'year', 'trim' in call
bird_name = dict()

# print "inputs:"

for i in arguments.keys():
	# print i, ' ',arguments[i].value
	bird_name[i] = arguments[i].value
# 
# #Reading data

bird_name = bird_name['name']

# # print sys.prefix
# # print sys.version
#print bird_name

try:
	texts, links, locations, image_links = mastercontroller.main_2(bird_name) #Calling mastercontroller
except Exception as e:
	outfile = open("errors.log", "a")
	outfile.write(str(e))
	outfile.close()
	exit(1)

#responsedict = {}
#responsedict = OrderedDict()

rowdict = {}
rowdict = OrderedDict()
rowdict['extracted_text'] = texts
rowdict['wikipedia_link'] = links
rowdict['location_info'] = locations
rowdict['image_links'] = image_links

global_response = {}
global_response = OrderedDict()

global_response['result'] = True
global_response['data'] = rowdict #deal with corner cases
print (json.JSONEncoder().encode(global_response))