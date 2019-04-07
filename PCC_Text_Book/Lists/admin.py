from Lists.user_1 import Users


class Admin(Users):
	"""A super with admin privileges"""
	
	def __init__(self, first_name, last_name, username, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, location)
		
		# Initialize an empty set of privileges.
		self.privileges = Privileges()


class Privileges():
	"""A class to store an admin's privileges."""
	
	def __init__(self, privileges=[]):
		"""Initialize the attribute"""
		self.privileges = privileges
	
	def show_privileges(self):
		"""Display the privileges this administration has."""
		print(f"Privileges:")
		
		for privilege in self.privileges:
			print(f" - {privilege}")