class Users():
	"""Represent a simple user profile."""
	
	def __init__(self, first_name, last_name, username, location):
		"""Initialize the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = first_name + last_name + '@gmail.com'
		self.login_attempts = 0
		self.location = location.title()
	
	def describe_user(self):
		"""Display a summary of user's information"""
		print( f"{self.first_name} {self.last_name}" )
		print( f"\t Username: {self.username}" )
		print( f"\t Email: {self.email}" )
		print( f"\t Location: {self.location}" )
	
	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print( f"Welcome back, {self.username}" )
	
	def increment_login_attempts(self):
		"""Increment the value of login_attempts."""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0