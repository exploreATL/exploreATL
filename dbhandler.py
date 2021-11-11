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
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)
		try:
			cursor.execute('''CREATE TABLE user_table (
			    USER_ID varchar(100),
			    PASS varchar(100),
			    LIST text[],
			    PRIMARY KEY (USER_ID)
				);''')
			connect.commit()
			connect.close()
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
	    pass : String
	    	A String object for the user password. required
	    artist_list: List
	    	A List object that contains the list of 'artist_id's to add to the table. required

		"""

		# Hash password for storage
		hashed_pass = hashlib.md5(password.encode())

		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)
		try:
			cursor.execute(
	    		"""
	    		INSERT INTO user_table(USER_ID,PASS,LIST)
	    		VALUES (%s, %s, %s)
	    		""",
	    		(user_id, hashed_pass, places_list)
			)
			connect.commit()
			connect.close()
			return
		except ValueError:
			print("Table Intsert error. Either already exist or other.")
			connect.commit()
			connect.close()
			pass


	def lookup_user(self, user_id:str, password:str): 
		"""
		Used the psycopg2 init functions to lookup user object if one exist. If it does throw error and pass.

		Parameters
	    ----------
	    user_id : String
	        A String object for the user_id in table. required
	    password:str
	    	A String object for the user password. required

	    Returns : table object with user_id and list of 'artist_id's

		"""
		connect = self.initdbconnect(self)
		cursor = self.initdbcursor(self, connect)
		try:
			cursor.execute("SELECT * from user_table WHERE USER_ID=%s", (user_id, ))
			info = cursor.fetchall()
			connect.commit()
			connect.close()
			return info
		except ValueError:
			print("Table Lookup error. Either does not exist or other.")
			connect.commit()
			connect.close()
			pass


	def insert_list(user_id:str, places_list:list):
		#TODO
		pass

	def update_list(user_id:str, places_list:list):
		#TODO
		pass

