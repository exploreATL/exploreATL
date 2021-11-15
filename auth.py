"""
Project 2
Explore ATL
GSU CSC 4350 Software Engineering
Fall 2021

This is the 'auth.py' python file for the Project 2.
This file includes the neccisary functinality to implement a user function in the app.


Python3.9 was used for this assignment.
Please run with the Linux or macOS 3.9 version of the python interpreter.

If there are any questions, please contact me at 'mroussell1@student.gsu.edu'.
MIT Education License Preferred
"""

from flask_login import UserMixin

# Make Interface Class object User from UserMixin
class User(UserMixin):

	# Class init
	def __init__(self, id:str, user_list:list, check_list:list, review_list:list):
		self.id = id
		self.user_list = user_list
		self.check_list = check_list
		self.review_list = review_list

	# requires get
	def get(id):
		return id

