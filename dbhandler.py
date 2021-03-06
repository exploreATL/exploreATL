"""
Project 2
Explore ATL
GSU CSC 4350 Software Engineering
Fall 2021

This is the 'dbhandler' python file for the Project 2.
This file handles all of the functionality involved with CRUD in the database.

Python3.9 was used for this assignment.
Please run with the Linux or macOS 3.9 version of the python interpreter.

If there are any questions, please contact us at 'exploreatl.devs@gmail.com'.
MIT Eduation License Preferred
"""
import os
import psycopg2
import hashlib
from dotenv import load_dotenv

class DBHandler:
	'''
	Class def for a database handler. 
	Handles interaction with postgresql database and CRUD functionality for the database.
	'''
	def initdbconnect(self):
		"""
		Loads Database URL and then connect to database and initializes the psycopg2 DATABASE Connection object.
		"""
		load_dotenv()
		try:
			DATABASE_URL = os.getenv('DATABASE_URL')
			conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			return conn
		except ValueError:
			print("Please use your own DATABASE_URL. Define it in to your .env file!")
			quit()


	def initdbcursor(self, conn):
		"""
		Initializes the psycopg2 DATABASE Curser for DATABASE Interaction.
		"""
		cur = conn.cursor()
		return cur


	def create_user_table(self):
		"""
		Used the psycopg2 init functions to create table if one does not already exist. If it does throw error and pass.

		"""
		# Create connection and cursor
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)
		try:
			cursor.execute('''CREATE TABLE test_table3 (
			    USER_ID varchar(100),
			    PASS varchar(100),
			    LOCATION varchar(100),
			    TYPE varchar(100),
			    LIST text[5],
			    BEEN bool[5],
			    REVIEW text,
			    PRIMARY KEY (USER_ID)
				);''')
			connect.commit()
			connect.close()
			print("Created Table Successfully")
			return
		except ValueError:
			print("Table Creation error. Either already exist or other.")
			connect.commit()
			connect.close()
			pass


	def insert_user(self, user_id:str, password:str, places_list:list):
		"""
		Used the psycopg2 init functions to insert user object if one does not already exist. If it does throw error and pass.

		Parameters
	    ----------
	    user_id : String
	        A String object for the user_id in table. required
	    password : String
	    	A String object for the user password. required
	    places_list: List
	    	A List object that contains the list of place names to add to the table. required
	
		Returns:
			0 if added succesfully and 1 is there was an error
		"""



		# Hash password for storage
		hashed_obj = hashlib.md5(password.encode())
		hashed_pass = hashed_obj.hexdigest()

		# Create connection and cursor
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)

		# Check if user already exists
		cursor.execute("SELECT * from test_table3 WHERE USER_ID=%s", (user_id, ))
		info = cursor.fetchall()

		if info:
			return 1

		# Insert user into user table
		try:
			cursor.execute(
	    		"""
	    		INSERT INTO test_table3(USER_ID,PASS,LIST)
	    		VALUES (%s, %s, %s)
	    		""",
	    		(user_id, hashed_pass, places_list)
			)
			connect.commit()
			connect.close()
			return 0
		except ValueError:
			print("Table Intsert error. Either already exist or other.")
			connect.commit()
			connect.close()
			return 1


	def lookup_user(self, user_id:str, password:str): 
		"""
		Used the psycopg2 init functions to lookup user object if one exist. If it does throw error and pass.

		Parameters
	    ----------
	    user_id : String
	        A String object for the user_id in table. required
	    password:str
	    	A String object for the user password. required

	    Returns : table object with user's info object, or 1 if there was error

		"""
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)

		# Hash Password
		hashed_obj = hashlib.md5(password.encode())
		hashed_pass = hashed_obj.hexdigest()

		# Check for user
		try:
			cursor.execute("SELECT * from test_table3 WHERE USER_ID=%s", (user_id, ))
			info = cursor.fetchall()
			if not info:
				return 1
			if info[0][1] == hashed_pass:
				connect.commit()
				connect.close()
				return info
			return 1
		except ValueError:
			print("Table Lookup error. Either does not exist or other.")
			connect.commit()
			connect.close()
			return 1


	def update_list(self, user_id:str, location:str, loc_type:str, places_list:list, been:list, review:str):
		"""
		Used the psycopg2 init functions to insert user's list and data. If it does throw error and pass.

		Parameters
	    ----------
	    user_id : String (required)
	        A String object for the user_id in table. 
	    loc_type : String (required)
	    	A String object that indicates the type of locations given
	    places_list: List (required)
	    	A List object that contains the list of place namess to add to the table. 
	    been : List (required)
	    	A List object that indicates in same order as places_list which places have been visited
		review : String (required)
			A String object that has the 

		Returns:
			0 if added succesfully and 1 is there was an error
		"""

		# if arrays are too large, trim them
		if len(places_list) > 5:
			places_list = places_list[5:]
		if len(been) > 5:
			been = been[5:]

		# init connection and cursor
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)

		# find user_id
		cursor.execute("SELECT * from test_table3 WHERE USER_ID=%s", (user_id, ))
		info = cursor.fetchall()

		# if no user exist, return error code 1
		if info == None:
			return 1

		# update user values in user table
		try:
			cursor.execute(
	    		"""
	    		UPDATE test_table3
	    		SET LOCATION=%s, TYPE=%s, LIST=%s, BEEN=%s, REVIEW=%s
	    		WHERE USER_ID=%s
	    		""",
	    		(location, loc_type, places_list, been, review, user_id, )
			)
			connect.commit()
			connect.close()
			print(f'Data Updated for {user_id}')
			return 0
		except ValueError:
			print("Table Intsert error. Either already exist or other.")
			connect.commit()
			connect.close()
			return 1


	def update_review(self, user_id:str, been:list, review:str):
		"""
		Used the psycopg2 init functions to insert user's list and data. If it does throw error and pass.

		Parameters
	    ----------
	    user_id : String (required)
	        A String object for the user_id in table. 
	    places_list: List (required)
	    	A List object that contains the list of place namess to add to the table. 
	    been : List (required)
	    	A List object that indicates in same order as places_list which places have been visited
		review : String (required)
			A String object that has the 

		Returns:
			0 if added succesfully and 1 is there was an error
		"""

		# if arrays are too large, trim them
		if len(been) > 5:
			been = been[5:]

		# init connection and cursor
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)

		# find user_id
		cursor.execute("SELECT * from test_table3 WHERE USER_ID=%s", (user_id, ))
		info = cursor.fetchall()
		print(info)
		# if no user exist, return error code 1
		if info == None:
			print("No User Info")
			return 1
		
		# update user values in user table
		try:
			cursor.execute(
	    		"""
	    		UPDATE test_table3
	    		SET BEEN=%s, REVIEW=%s
	    		WHERE USER_ID=%s
	    		""",
	    		(been, review, user_id)
			)
			connect.commit()
			connect.close()
			print(f"Data Updated for  user '{user_id}'")
			return 0
		except ValueError:
			print("Table Intsert error. Either already exist or other.")
			connect.commit()
			connect.close()
			return 1



### USED FOR TESTING ###
# DBHandler.create_user_table(DBHandler)
# username = 'admin012341234'
# password = 'password'
# near_places = ["Hyatt Regency Atlanta", "Hard Rock Cafe", "The Sun Dial Restaurant", "Bar & View", "Ray's In the City"]
# loc_type = "restaurant"
# location = "midtown atlanta"
# been = [True, False, False, False, False]
# review = "I liked a place because of a thing that involved other things around that place and things that were inside that place"

# DBHandler.insert_user(DBHandler, username, password, near_places)
# DBHandler.update_list(DBHandler, username, location, loc_type, near_places, been, review)
# print("did the update")
# result = DBHandler.lookup_user(DBHandler, username, password)
# print(result[0][1])

# #
# userid = "123"
# been = [True, False, False, False, True]
# review = "This place would be great if the database started to work."
# DBHandler.update_review(DBHandler, userid, been, review)

