class Restaurant():
	"""A class representing a class."""


	def __init__(self, restaurant_type, cuisine_type):
		"""Initialize the restaurant"""
		self.restaurant_type = restaurant_type.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 0


	def describe_restaurant(self):
		"""Display the summary of the restaurant"""
		message = f"Our restaurant '{self.restaurant_type}' serves wonderful '{self.cuisine_type}'. "
		print( message )


	def open_restaurant(self):
		"""Display the restaurant is open."""
		restaurant_open = f"{self.restaurant_type} restaurant is open. Come on in!!!"
		print( restaurant_open )


	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served


	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served
