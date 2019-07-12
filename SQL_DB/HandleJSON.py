#!/usr/bin/env python

import json
import sqlite3

from DatabaseTools.SetFirst import setFirst
from DatabaseTools.SetLast import setLast
from DatabaseTools.SetUser import setUser

# from DatabaseTools import SetUser

jobj = {
	"Handle": '8',
	
	"UserInfo" : {
	  "Id": "",
	  "FirstName": "Daniel",	
	  "LastName": "ManLost",
	  "UserName": "Danskiboy",
	  "Email": "d@gmail.com",
	  "Password": "lolol",
	  "PIN": "1234",
	  "Phone": "2023034004",
	  "Friends": "",
	  "Connection": ""
	},

	"MadeItMessage" : "ImDead"
	}

def handleJSON(jObject):
	y = jObject

	# Get Data from JSON
	handle = int(y["Handle"])
	print("Handle # is: {}".format(handle))
	
	userInfo = y["UserInfo"]
	message = y["MadeItMessage"]

	if handle == 0:
		# create a new user
		print("# create a new user")
		# TODO

	elif handle == 1:
		# User 'MadeIt' - Contact friends
		print("# User 'MadeIt' - Contact friends")
		# TODO

	elif handle == 2:
		# Add Freinds to user
		print("# Add Freinds to user")
		# TODO
	
	elif handle == 3:
		# Remove friend from users list
		print("# Remove friend from user's list")
		# TODO

	elif handle == 4:
		# User 'MadeIt' - Contact friends
		print("# User 'MadeIt' - Contact friends")
		# TODO

	elif handle == 5:
		# Delete a User's account
		print("# Delete a User's account")


	elif handle == 6:
		# Set User's First Name
		# print("# Set User's First Name")
		print(userInfo["Email"], userInfo["FirstName"])
		setFirst(userInfo["Email"], userInfo["FirstName"])
		

	elif handle == 7:
		# Set User's Last Name
		# print("# Set User's Last Name")
		print(userInfo["Email"], userInfo["LastName"])
		setLast(userInfo["Email"], userInfo["LastName"])


	elif handle == 8:
		# Set user's UserName
		print("# Set user's UserName")

		print(userInfo["Email"], userInfo["UserName"])
		setUser(userInfo["Email"], userInfo["UserName"])

handleJSON(jobj)
