"""9-1: Restaurant"""
"""Make a class called Restaurant. The __init__() method for Restaurant should store two
attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
that prints these two pieces of information, and a method called open_restaurant() that prints
a message indicating that the restaurant is open."""

"""Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods."""


class Restaurant():
	"""A class representing a class."""
	def __init__(self, restaurant_type, cuisine_type):
		"""Initialize the restaurant"""
		self.restaurant_type = restaurant_type.title()
		self.cuisine_type = cuisine_type.title()
		
	def describe_restaurant(self):
		"""Display the summary of the restaurant"""
		message = f"Our restaurant '{self.restaurant_type}' serves wonderful '{self.cuisine_type}'. "
		print(message)
	
	def open_restaurant(self):
		"""Display the restaurant is open."""
		restaurant_open = f"{self.restaurant_type} restaurant is open. Come on in!!!"
		print(restaurant_open)
		

restaurant = Restaurant('the mean quenn', 'pizza')
print(f"Our restaurant name: {restaurant.restaurant_type}")
print(f"**************************************************************************************")
print(f"Our cuisine type: {restaurant.cuisine_type}")
print(f"**************************************************************************************")

restaurant.describe_restaurant()
print(f"**************************************************************************************")
restaurant.open_restaurant()
print(f"**************************************************************************************")

"""9-2: Three Restaurants"""
"""Start with your class from Exercise 9-1. Create three different instances from the class,
and call describe_restaurant() for each instance."""


class Restaurant():
	"""A class representing a class."""
	
	def __init__(self, restaurant_type, cuisine_type):
		"""Initialize the restaurant"""
		self.restaurant_type = restaurant_type.title()
		self.cuisine_type = cuisine_type.title()
	
	def describe_restaurant(self):
		"""Display the summary of the restaurant"""
		message = f"Our restaurant '{self.restaurant_type}' serves wonderful '{self.cuisine_type}'. "
		print( message )
	
	def open_restaurant(self):
		"""Display the restaurant is open."""
		restaurant_open = f"{self.restaurant_type} restaurant is open. Come on in!!!"
		print(restaurant_open)


restaurant_1 = Restaurant('the mean queen', 'pizza')
print(f"Our restaurant name: {restaurant_1.restaurant_type}.")
print(f"Our cuisine type: {restaurant_1.cuisine_type}")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print(f'****************************************************************************')
restaurant_2 = Restaurant('ludwig\'s bistro', 'seafood')
print(f"Our restaurant name: {restaurant_2.restaurant_type}.")
print(f"Our cuisine type: {restaurant_2.cuisine_type}")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print(f'****************************************************************************')
restaurant_3 = Restaurant('mango thai', 'thai food')
print(f"Our restaurant name: {restaurant_3.restaurant_type}.")
print(f"Our cuisine type: {restaurant_3.cuisine_type}")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
print(f'****************************************************************************')


"""9-3: Users"""

"""Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user."""

"""Create several instances representing different users, and call both methods for each user."""


class Users():
	"""Represent a simple user profile."""
	def __init__(self, first_name, last_name, username, location):
		 """Initialize the user."""
		 self.first_name = first_name.title()
		 self.last_name = last_name.title()
		 self.username = username
		 self.email = first_name + last_name + '@gmail.com'
		 self.location = location.title()
		
	def describe_user(self):
		"""Display a summary of user's information"""
		print(f"{self.first_name} {self.last_name}")
		print(f"\t Username: {self.username}")
		print(f"\t Email: {self.email}")
		print(f"\t Location: {self.location}")
	
	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"Welcome back, {self.username}")
	
		
user_1 = Users('paavan', 'gopala', 'iampaavan', 'bangalore')
user_1.describe_user()
user_1.greet_user()
print(f"*********************************************************************")
user_2 = Users('manjula', 'subramanyam', 'manjula_s', 'bangalore')
user_2.describe_user()
user_2.greet_user()
print(f"*********************************************************************")
user_3 = Users('thilak', 'raj', 'thilak_raj', 'bangalore')
user_3.describe_user()
user_3.greet_user()
print(f"*********************************************************************")


"""9-4: Number Served"""
"""Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served
with a default value of 0. Create an instance called restaurant from this class. Print the number
of customers the restaurant has served, and then change this value and print it again."""

"""Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again."""

"""Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business."""


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
		print(message)
	
	def open_restaurant(self):
		"""Display the restaurant is open."""
		restaurant_open = f"{self.restaurant_type} restaurant is open. Come on in!!!"
		print(restaurant_open)
		
	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served
		
	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served
		
		
restaurant_4 = Restaurant('boston shawarma', 'chicken shawarmaas')
restaurant_4.describe_restaurant()
restaurant_4.open_restaurant()
print(f'***********************************************************************************************')
print(f'Initially served {restaurant_4.number_served} of customers.')
print(f'***********************************************************************************************')
service = restaurant_4.number_served = 10
print(f"First time service done: {service}")
print(f'***********************************************************************************************')
restaurant_4.set_number_served(200)
print(f'Total served until now: {restaurant_4.number_served}')
print(f'***********************************************************************************************')
restaurant_4.increment_number_served(500)
print(f'Final servings at the end of business day: {restaurant_4.number_served}')
print(f'***********************************************************************************************')

"""9-5: Login Attempts"""
"""Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called
increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts()
that resets the value of login_attempts to 0."""

"""Make an instance of the User class and call increment_login_attempts() several times. Print the value of
login_attempts  to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0."""


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
		print(f"{self.first_name} {self.last_name}")
		print(f"\t Username: {self.username}")
		print(f"\t Email: {self.email}")
		print(f"\t Location: {self.location}")
	
	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"Welcome back, {self.username}")

	def increment_login_attempts(self):
		"""Increment the value of login_attempts."""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0
		

user_1 = Users('paavan', 'gopala', 'iampaavan', 'bangalore')
user_1.describe_user()
user_1.greet_user()
print(f"*********************************************************************")
print(f"Making 3 login attempts")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Total number of login attempts: {user_1.login_attempts}")
print(f'*********************************************************************')
print(f"Reset login attempts")
user_1.reset_login_attempts()
print(f"Resetting the login attemps: {user_1.login_attempts}")
print(f'*********************************************************************')

"""9-6: Ice Cream Stand"""
"""An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits
from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work;
just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method."""


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
		print(message)
	
	def open_restaurant(self):
		"""Display the restaurant is open."""
		restaurant_open = f"{self.restaurant_type} restaurant is open. Come on in!!!"
		print(restaurant_open)
	
	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served
	
	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served


class IceCreamStand(Restaurant):
	"""Represent an ice-cream stand"""
	def __init__(self, restaurant_type, cuisine_type='ice cream'):
		"""Initialize the ice cream stand"""
		super().__init__(restaurant_type, cuisine_type)
		self.flavors = []
		
	def show_flavors(self):
		"""Display the flavors"""
		print(f"We have the following flavors.")
		for flavor in self.flavors:
			print(flavor.title())
			

ice = IceCreamStand('The Big One')
ice.flavors = ['vanilla', 'chocolate', 'black cherry']
print(f'***********************************************************************')
ice.describe_restaurant()
print(f'***********************************************************************')
ice.show_flavors()
print(f'***********************************************************************')

"""9-7: Admin"""
"""An administrator is a special kind of user. Write a class called Admin that inherits from the User
class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that
stores a list of strings like "can add post", "can delete post", "can ban user", and so on. WRite a method
called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin,
and call your method."""


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
		print(f"{self.first_name} {self.last_name}")
		print(f"\t Username: {self.username}")
		print(f"\t Email: {self.email}")
		print(f"\t Location: {self.location}")
	
	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"Welcome back, {self.username}")
	
	def increment_login_attempts(self):
		"""Increment the value of login_attempts."""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0


class Admin(Users):
	"""A super with admin privileges"""
	def __init__(self, first_name, last_name, username, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, location)
		self.privileges = []
		
	def show_privileges(self):
		"""Display the privileges this administration has."""
		print(f"Privileges:")
		for privilege in self.privileges:
			print(f" - {privilege}")
			

admin = Admin('eric', 'matthes', 'e_matthes', 'alaska')
admin.describe_user()
admin.privileges = ['can reset passwords', 'can moderate discussions', 'can suspend accounts']
print(f'**************************************************************************')
admin.greet_user()
print(f'**************************************************************************')
admin.show_privileges()
print(f'**************************************************************************')


"""9-8: Privileges"""
"""Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of
strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges."""


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
		print(f"{self.first_name} {self.last_name}")
		print(f"\t Username: {self.username}")
		print(f"\t Email: {self.email}")
		print(f"\t Location: {self.location}")
	
	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"Welcome back, {self.username}")
	
	def increment_login_attempts(self):
		"""Increment the value of login_attempts."""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0


class Admin(Users):
	"""A super with admin privileges"""
	
	def __init__(self, first_name, last_name, username, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, location)
		
		#Initialize an empty set of privileges.
		self.privileges = Privileges()
	
	
class Privileges():
	"""A class to store an admin's privileges."""
	def __init__(self, privileges=[]):
		"""Initialize the attribute"""
		self.privileges = privileges
		
	def show_privileges(self):
		"""Display the privileges this administration has."""
		print(f"Privileges:")
		if self.privileges:
			for privilege in self.privileges:
				print(f" - {privilege}")
		else:
			print(f"This user has no privileges.")
			

admin_1 = Admin('eric', 'matthes', 'e_matthes', 'alaska')
admin_1.describe_user()
print(f"*****************************************************************************")
admin_1.greet_user()
print(f"*****************************************************************************")
admin_1.privileges.show_privileges()
print(f"*****************************************************************************")
admin_1_privileges = ['can reset passwords', 'can moderate discussions', 'can suspend accounts']
print(f"*****************************************************************************")
admin_1.privileges.privileges = admin_1_privileges
admin.show_privileges()
print(f"*****************************************************************************")


"""9-9: Battery Upgrade"""
"""Use the final version of electric_car.py from this section. Add a method to the Battery class
called upgrade_battery(). This method should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after
upgrading the battery. You should see an increase in the car’s range."""


class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, manufacturer, model, year):
		"""Initialize the attributes to describe a car."""
		self.manufacturer = manufacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.manufacturer} {self.model}"
		return long_name
	
	def read_odometer(self):
		"""Print a statement showing a car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value. Reject the change
		if it attempts to roll the odometer back """
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print(f"Cannot roll back odometer reading.")
			
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		
		
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=60):
		"""Initialize the battery attribute."""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")
		
	def get_range(self):
		"""Print the statement about the range this battery provides."""
		
		if self.battery_size == 60:
			range = 140
			
		elif self.battery_size == 85:
			range = 185
			
		message = f"This car can go approximately {range}"
		message += " miles on full charge."
		print(message)
		
	def upgrade_battery(self):
		"""Upgrade the battery if possible"""
		
		if self.battery_size == 60:
			self.battery_size = 85
			print(f"Upgraded the battery to 85 kWh.")
			
		else:
			print(f"This battery is already upgraded.")
	
	
class ElectricCar(Car):
	"""Models aspects of a car, specifically to electric vehicles."""
	
	def __init__(self, manufacturer, model, year):
		"""Initialize the attributes of the parent class
		and initialize the attributes of electric car."""
		
		super().__init__(manufacturer, model, year)
		self.battery = Battery()
		

print(f"Make an electric car, and check the battery.")
my_tesla = ElectricCar('telsa', 'model s', 2016)
my_tesla.battery.describe_battery()
print(f'****************************************************************************')
print(f'Upgrade the battery, and check it.')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
print(f'****************************************************************************')
print(f'Trying to upgrade the battery second time.')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
print(f'****************************************************************************')


"""9-13: OrderedDict Rewrite"""
"""Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary.
Rewrite the program using the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary."""

"""Note: In Python 3.6, dictionaries store keys in order. However, this is not guaranteed to work in
all versions of Python, so you should still use an OrderedDict when you need key-value pairs to be
stored in a particular order."""

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for key, value in glossary.items():
	print(f"{key.title()}: {value}")


"""9-14: Dice"""
"""The module random contains functions that generate random numbers in a variety of ways.
The function randint() returns an integer in the range you provide. the following code returns a
number between 1 and 6: from random import randint --> x = randint(1, 6)"""

from random import randint


class Dice():
	"""Represent a die, which can be rolled."""
	def __init__(self, sides=6):
		"""Initialize the die."""
		self.sides = sides
		
	def roll_dice(self):
		"""return the number between 1 and the number of sides."""
		return randint(1, self.sides)
	

d6 = Dice()
results = []

for num_roll in range(10):
	result = d6.roll_dice()
	results.append(result)
print(f'10 rolls of a 6-sided dice.')
print(results)
print(f'*********************************************************************')

d10 = Dice(sides=20)
my_results = []

for test in range(10):
	check = d10.roll_dice()
	my_results.append(check)
print(f'10 rolls of a 20-sided dice.')
print(my_results)
print(f'*********************************************************************')

