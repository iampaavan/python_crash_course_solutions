"""8-1: Message"""
"""Write a function called display_message() that prints one sentence telling everyone what
you are learning about in this chapter. Call the function, and make sure the message displays correctly."""


def display_message():
	"""Display a message about what i'm learning."""
	message = f"I'm learning to store code in functions."
	print(message)
	
	
display_message()
print(f'********************************************************************************************')

"""8-2: Favorite Book"""
"""Write a function called favorite_book() that accepts one parameter, title. The function should print
a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""


def favorite_book(title):
	"""Display a message about someone's favorite book."""
	print(f"{title} is one of my favorite books.")
	
	
favorite_book('Secret Stories')
print(f'**********************************************************************************************')

"""8-3: T-Shirt"""
"""Write a function called make_shirt() that accepts a size and the text of a message that should be printed
on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it."""

"""Call the function once using positional arguments to make a shirt. Call the function a
second time using keyword arguments."""


def make_shirt(size, message):
	"""Summarize the t-shirt that's going to be made."""
	print(f"I'm going to make a {size} sized t-shirt.")
	print(f"It will say {message}.")
	
	
make_shirt('large', 'I love Python!!')
print(f'************************************************************************************************************')
make_shirt(message='readability counts.', size='medium')
print(f'************************************************************************************************************')

"""8-4: Large Shirts"""
"""Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""


def make_tshirt(size='large', message='I love Python'):
	"""Summarize the t-shirt that's going to be made."""
	print(f"I'm going to make a {size} sized t-shirt.")
	print(f"It will say {message}.")
	
	
make_tshirt()
print(f'***********************************************************************************************************')
make_tshirt(size='medium')
print(f'***********************************************************************************************************')
make_tshirt(size='small', message='Programmers are loopy.')
print(f'***********************************************************************************************************')

"""8-5: Cities"""
"""Write a function called describe_city() that accepts the name of a city and its country. The function should print
 a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your
 function for three different cities, at least one of which is not in the default country."""


def describe_cities(city, country='chile'):
	"""Describe a city."""
	print(f"{city.title()} is in {country.title()}")
	
	
describe_cities('santiago')
print(f'****************************************************************************************')
describe_cities('reykjavik', 'iceland')
print(f'****************************************************************************************')
describe_cities('punta arenas')
print(f'****************************************************************************************')

"""8-6: City Names"""
"""Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: “Santiago, Chile”"""


def city_country(city, country):
	"""Return a string like “Santiago, Chile”."""
	return f"{city.title()}, {country.title()}."


city_1 = city_country('santiago', 'chile')
print(city_1)
print(f'*****************************************************************************************')
city_2 = city_country('bangalore', 'india')
print(city_2)
print('******************************************************************************************')
city_3 = city_country('boston', 'massachusetts')
print(city_3)
print(f'*****************************************************************************************')

"""8-7: Album"""
"""Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary
containing these two pieces of information. Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly"""


def make_album(artist, title):
	"""Build a dictionary containing information about an album."""
	build_dict = {
		'artist': artist.title(),
		'title': title.title()
}
	return build_dict


album_1 = make_album('metallicca', 'ride the lightning')
print(album_1)
print(f'**********************************************************************')
album_2 = make_album('beethoven', 'ninth symphony')
print(album_2)
print(f'**********************************************************************')
album_3 = make_album('willie nelson', 'red-headed stranger')
print(album_3)
print(f'**********************************************************************')

"""Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
If the calling line includes a value for the number of tracks, add that value to the album’s dictionary.
Make at least one new function call that includes the number of tracks on an album."""


def make_album(artist, title, tracks=0):
	"""Build a dictionary containing the information about an album"""
	build_dictionary = {
		'article': artist.title(),
		'title': title.title()
}
	if tracks:
		build_dictionary['tracks'] = tracks
	return build_dictionary
	
	
album_1 = make_album('metallica', 'ride the lightning')
print(album_1)
print(f'**********************************************************************')

album_2 = make_album('beethoven', 'ninth symphony')
print(album_2)
print(f'**********************************************************************')

album_3 = make_album('willie nelson', 'red-headed stranger')
print(album_3)
print(f'**********************************************************************')

album_4 = make_album('iron maiden', 'piece of mind', tracks=8)
print(album_4)
print(f'**********************************************************************')

"""8-8: User Albums"""
"""Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop."""


def make_album(artist, title, tracks=0):
	"""Build a dictionary containing information about an album"""
	build_dictionary = {
		'artist': artist,
		'title': title
}
	if tracks:
		build_dictionary['tracks'] = tracks
	return build_dictionary


# Prepare for the prompts
title_prompt = f"What album are you thinking of?"
album_prompt = f"\nWho's the artist?"

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
	
	title = input(title_prompt)
	if title == 'quit':
		break
	
	artist = input(album_prompt)
	if artist == 'quit':
		break
		
	album_5 = make_album(artist, title)
	print(album_5)
	
print(f"Thanks for responding.")
print(f'**************************************************************************')

"""8-9: Magicians"""
"""Make a list of magician’s names. Pass the list to a function called show_magicians(),
which prints the name of each magician in the list."""


def make_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())
		
		
magicians = ['harry houdini', 'david blaine', 'teller']
make_magicians(magicians)
print(f'***************************************************************************')


"""8-11: Unchanged Magicians"""
"""Start with your work from Exercise 8-10. Call the function make_great() with a copy
of the list of magicians’ names. Because the original list will be unchanged, return
the new list and store it in a separate list. Call show_magicians() with each list to
show that you have one list of the original names and one list with the Great added to
each magician’s name."""


def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())
		
		
def make_great(magicians):
	"""Add 'the Great!' to each magician's name."""
	# Build a new list to hold the great magicians.
	great_magicians = []

	# Make each magician great, and add it to great_magicians.
	while magicians:
		magician = magicians.pop()
		great_magician = f"{magician} the Great."
		great_magicians.append(great_magician)
		
	# Add the great magicians back to magicians.
	for great_magician in great_magicians:
		magicians.append(great_magician)
		
	return magicians


magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)
print()

print(f"Great Magicians: ")
great_magician = make_great(magicians[:])
show_magicians(great_magician)

print("\nOriginal magicians:")
show_magicians(magicians)
print(f"********************************************************************")

"""8-12: Sandwiches"""
"""Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter
 that collects as many items as the function call provides, and it should print a summary of the sandwich that
 is being ordered. Call the function three items, using a different number of arguments each time."""


def make_sandwich(*items):
	"""Make a sandwich with the given items"""
	print(f"I'll make you a great sandwich.")
	for item in items:
		print(f" ....adding {item} to your sandwich")
	print(f"Your sandwich is ready!!!")
	
	
make_sandwich('roasted beef', 'cheddar cheese', 'lettuce', 'honey dijon')
print(f"***************************************************************")
make_sandwich('turkey', 'apple slices', 'honey mustard')
print(f"***************************************************************")
make_sandwich('peanut butter', 'strawberry jam')
print(f"***************************************************************")

"""8-14: Cars"""
"""Write a function that stores information about a car in a dictionary. the function should
 always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments.
 Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
 Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)"""


def make_car(manufacturer, model, **options):
	"""Make a dictionary representing a car."""
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title()
}
	for key, value in options.items():
		car_dict[key] = value
	
	return car_dict


my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
print(f"*******************************************************************")
car = make_car('honda', 'accord', year=1992, color='red', headlights='popup')
print(car)
print(f"*******************************************************************")
