# User Guide

## Folder Dependencies
- python3
- sqlite3

##  About
This folder contains files to create and interact with the user info database. The intent is to pull these files from GitLab onto an instance of a cloud Linux Server.
From there, the database can be setup and and interacted with using the files in this
folder.


There are a number of a number of file found in the folder. Their names and puropses will be listed below:

- SetupDB.py > Running this creates UserInfo.db - which is a file containing information about clients
    of MadeIt app. The DB is managed using sqlite3, and stores informatoin in the main table named Users. 
    See further information about the database below.

- CreateClient.py > This file contains a simple interface for creating a client in the database using the information
    entered by the user of MadeIt when creating an account. 

- DeleteUser.py > Used to remove all of a client's info from the database should they delete thier account.

- AddFriend.py > When a user picks friends to communicate with using MadeIt, the friends will be updated in the database using the interface provided in this script. Friends are identified by thier ID number in db.

- DeleteFriend.py > this provides an interface used to remove a friend from the user's friends list in database. 

- DeleteAllFriends.py > this provides an interface used to remove all current friends from the user's friends list in database. Kind of a 'reset' for the freinds list. Current idea is that this could be performed everytime the user presses the MadeIt button.

- AddPIN.py > Allows a PIN to be set to the PIN column of the passed in user.

- CheckEmail.py > this checks to see if the user exists in the database using thier email as the unique identifier. If existing, the user's ID number is returned as well as thier existing status (boolean true). Though this is used more as a helper to the above mentioned, it is commonly occuring and should be noted.

- UserInfo.db > is a sample database for this project. 

- Variables.py > this contains the hard-coded varaible definitions that are used across all the other files. These definitions can be imported using `from Variables import *`


More descriptions of the functions will be added within each file soon. In the mean time, a look at each file's function definitions should give some clarity as to how they are used.


*The unmentioned files contained in this deirectory are "playground" files that aren't intended to be used in the overal project.

## Setup

1. Download the files from GitLab to machine or instance hosting the database. Ensure needed dependencies are installed.
2. Run SetupDB.py to create the database. Delete SetupDB.py after using. If this script is exectued agian, the database will be cleared and recreated.
3. Use the functions needed for interactions by main project by importing them to your project file.


## About the Database

The columns in the database and thier purposes are listed below:

- Id   > Contains a unique numerical identifier for each customer.
- Name > Clients username.
- Email > Clients email.
- Password > Clients password.
- PIN > 4 digit pin we could set for the user to verify thier ID when they press the made it button.
- Phone > clients phone.
- Friends > contains the Id of each user with whom the client is 'friends'.
- Connection > this could store data needed to connect with the clients mobile device. More of a place holder in case such as field is needed.

## Testing

Basic testing has yet to be performed on a cloud instance of the 
database. All testing has benn performed on locally on MacBook 
Pro. More information will be added about testing performed and
testing plans and proceedures soon.

It is recomended that the files be downloaded to a Mac or Linux for testing. Spend some time exploring the use of functions for interacting with database. TablePlus has been used to show/verify the results of each function are as intended. Your choice of tool for viewing a sqlite database will do for verification purposes.
