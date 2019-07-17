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

def handleJSON(jObject):
	y = jObject

	# Get Data from JSON
	handle = int(y["Handle"])
	print("Handle # is: {}".format(handle))
	
	userInfo = y["UserInfo"]
	message = y["MadeItMessage"]
	friendEmail = y["FriendEmail"]
	friendEmailList = y["FriendEmailList"]

	# always set the users IP
	setConnection(userInfo["Email"],userInfo["Connection"])


	if handle == 0:
		# create a new user
		# print("# create a new user")
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
		pass
		# print(getConnection(userInfo["Email"]))

# handleJSON(jobj)
