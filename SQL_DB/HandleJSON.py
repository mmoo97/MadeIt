#!/usr/bin/env python

import json
import sqlite3

from DatabaseTools.SetFirst import setFirst
from DatabaseTools.SetLast import setLast
from DatabaseTools.SetUser import setUser
from DatabaseTools.DeleteUser import deleteUser
from DatabaseTools.CreateUser import createUser
from DatabaseTools.DeleteAllFriends import deleteAllFriends
from DatabaseTools.DeleteFriend import deleteFriend
from DatabaseTools.AddFriend import addFriend
from DatabaseTools.SetConnection import setConnection
from DatabaseTools.GetConnection import getConnection
from DatabaseTools.CheckEmail import checkEmail

# from DatabaseTools import SetUser

jobj = {
	"Handle": '11',
	
	"UserInfo" : {
	  "Id": "",
	  "FirstName": "Daniel",	
	  "LastName": "Lowe",
	  "UserName": "toesareroses",
	  "Email": "d@gmail.com",
	  "Password": "lolol",
	  "PIN": "1234",
	  "Phone": "2023034004",
	  "Friends": "",
	  "Connection": "127.0.0.1"
	},

	"FriendEmail" : "s@gmail.com",

	"FriendEmailList" : ["c@gmail.com", "m@gmail.com"],

	"MadeItMessage" : "ImDead"
	}

# The JSON that gets sent back to app
retJSON = {
	"Handle":"0",

	"From":{
		"Userame":"",
		"FirstName":"",
		"LastName":"",
		"Email":""
	},
	
	"Message":"SentToUserByFrom"

}

def handleJSON(jObject):
	y = jObject

	# Get Data from JSON
	handle = int(y["Handle"])
	# print("Handle # is: {}".format(handle))
	
	userInfo = y["UserInfo"]
	message = y["MadeItMessage"]
	friendEmail = y["FriendEmail"]
	friendEmailList = y["FriendEmailList"]


	if handle == 0:
		# create a new user
		createUser(userInfo["FirstName"],userInfo["LastName"],userInfo["UserName"],\
			userInfo["Password"],userInfo["Email"])

	elif handle == 1:
		# User 'MadeIt' - Contact friends
		print("# User 'MadeIt' - Contact friends")
		# TODO

	elif handle == 2:
		# Add Freind to user
		addFriend(userInfo["Email"],friendEmail)
	
	elif handle == 3:
		# Remove friend from users list
		deleteFriend(userInfo["Email"],friendEmail)

	elif handle == 4:
		# Delete All Friends from User's Frineds list
		deleteAllFriends(userInfo["Email"])

	elif handle == 5:
		# Delete a User's account
		deleteUser(userInfo["Email"])

	elif handle == 6:
		# Set User's First Name
		setFirst(userInfo["Email"], userInfo["FirstName"])
		
	elif handle == 7:
		# Set User's Last Name
		setLast(userInfo["Email"], userInfo["LastName"])

	elif handle == 8:
		# Set user's UserName
		setUser(userInfo["Email"], userInfo["UserName"])

	elif handle == 9:
		# Add List of Friends to user
		for friend in friendEmailList:
			addFriend(userInfo["Email"],friend)

	elif handle == 10:
		# Delete List of Friends to User
		for friend in friendEmailList:
			deleteFriend(userInfo["Email"],friend)

	elif handle == 11:
		# Sign In
		# if user account exists return handle==3 to user  (theyre logged in)
		if checkEmail("Users",userInfo["Email"]):
			#Call Ishan's script to send JSON back to user
			pass
		# else Return Handle==2 to user  (need the create account screen)
		else:
			#Call Ishan's script to send JSON back to user
			pass

	# always set the users IP Connection Info
	setConnection(userInfo["Email"],userInfo["Connection"])


# handleJSON(jobj)
