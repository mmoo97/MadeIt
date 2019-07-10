#!/usr/bin/env python

import sqlite3
import json



jobj = {
	"Handle": '2',
	
	"UserInfo" : {
	  "Id": "",
	  "FirstName": "Daniel",	
	  "LastName": "Lowe",
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

	print(userInfo["LastName"])

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
		# TODO

	elif handle == 6:
		# Set User's First Name
		print("# Set User's First Name")
		# TODO

	elif handle == 6:
		# Set User's Last Name
		print("# Set User's Last Name")
		from SetLast import setLast
		setLast()
		# TODO

	elif handle == 6:
		# Set user's UserName
		print("# Set user's UserName")
		# TODO

handleJSON(jobj)






