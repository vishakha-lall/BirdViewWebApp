#!/usr/bin/python


import cgitb
import cgi
import os
import sys
from collections import OrderedDict
import json

cgitb.enable()

print ("Content-type: application/json")
print "Access-Control-Allow-Origin: *"
print

labels_file = open("output_labels.txt", "r")


labels_list = []
for lines in labels_file:
	labels_list.append(lines)

stripped_labels_list = []

for items in labels_list:
	temp_str = items
	temp_str = temp_str[4:-1]
	stripped_labels_list.append(temp_str)

global_response = {}
global_response = OrderedDict()

global_response['data'] = stripped_labels_list

print (json.JSONEncoder().encode(global_response))