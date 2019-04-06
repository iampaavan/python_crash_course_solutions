"""6-1: Person"""
"""Use a dictionary to store information about a person you know. Store their first name, last name, age,
 and the city in which they live. You should have keys such as first_name, last_name, age, and city.
 Print each piece of information stored in your dictionary."""

person = {
	'firstname': 'Paavan',
	'lastname': 'Gopala',
	'age': 27,
	'city': 'Bangalore'
}

for key, value in person.items():
	print(f'{key} --> {value}')

print(f'**************************************************************************************')
	
"""6-2: Favorite Numbers"""
"""Use a dictionary to store people’s favorite numbers. Think of five names,
and use them as keys in your dictionary. Think of a favorite number for each person,
and store each as a value in your dictionary. Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program."""

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000000,
    'maggie': 0,
    }

for key, value in favorite_numbers.items():
	if key not in favorite_numbers.items():
		pass
	print(f"{key.capitalize()}'s favorite number is {value}")

print(f'*************************************************************************************')

"""6-3: Glossary"""
"""A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary"""

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

for q, w in glossary.items():
	print(f'{q.capitalize()}: {w}')
	
print(f'*****************************************************************')

glossary.update(key='The first item in a key-value pair in a dictionary.')
glossary.update(value='An item associated with a key in a dictionary.')
glossary.update(conditionaltest='A comparison between two values.')
glossary.update(float='A numerical value with a decimal component.')
glossary.update(booleanexpression='An expression that evaluates to True or False.')

for t, y in glossary.items():
	print(f'{t.capitalize()}: {y}')

print(f'*****************************************************************')

"""6-5: Rivers"""
"""Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be 'nile': 'egypt'."""

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for o, p in rivers.items():
	print(f'The {o.capitalize()} runs through {p.title()}.')
print(f'*****************************************************************************')

print(f'The following rivers are included in this data set:')
for f in rivers.keys():
	print(f'- {f.capitalize()}')
print(f'*****************************************************************************')

print(f'The following countries are included in this data set:')
for g in rivers.values():
	print(f'- {g.capitalize()}')
print(f'*****************************************************************************')

"""6-6: Polling"""
"""Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some that are not."""

f_l = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for b, n in f_l.items():
	print(f'{b.capitalize()}\'s language is {n.capitalize()}.')
	
print(f'************************************************************************')

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
	if coder in f_l:
		print(f'Thank you for taking the poll, {coder.capitalize()} !')
	else:
		print(f'{coder.capitalize()}, What\'s your favorite programming language?')

print(f'*************************************************************************')

"""6-7: People"""
"""Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing
different people, and store all three dictionaries in a list called people. Loop through your list of people.
As you loop through the list, print everything you know about each person."""

# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
    }
people.append(person)

for peep in people:
	
	name = f"{peep['first_name'].capitalize()} {peep['last_name'].capitalize()}"
	age = f"{peep['age']}"
	city = f"{peep['city'].capitalize()}"
	print(f'{name}, of {city} is {age} years old.')
	
print(f'***************************************************************************')

"""6-8: Pets"""
"""Make several dictionaries, where the name of each dictionary is the name of a pet.
In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
Next, loop through your list and as you do print everything you know about each pet."""

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.

for pet in pets:
	print( f"Here's what I know about {pet['name'].capitalize()}: " )
	for key, value in pet.items():
		print(f"\t - {key.capitalize()} : {value}")

print(f'************************************************************************')

"""6-9: Favorite Places"""
"""Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person. To make this exericse a bit more interesting,
ask some friends to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places."""

my_favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for mykeys, myvalues in my_favorite_places.items():
	print(f"{mykeys.capitalize()} likes the following places: ")
	for myvalue in myvalues:
		print(f"- {myvalue.capitalize()}")
print(f"**************************************************************************")

"""6-10: Favorite Numbers"""
"""Modify your program from Exercise 6-2  so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers."""

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
	print(f"{name.capitalize()} likes the following numbers:")
	for number in numbers:
		print(f"- {number}")
		
print(f'***************************************************************************')

"""6-11: Cities"""
"""Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in,
its approximate population, and one fact about that city. The keys for each city’s dictionary
should be something like country, population, and fact. Print the name of each city and all of
the information you have stored about it."""

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himalaya',
        }
    }

for city, city_info in cities.items():
	country = city_info['country']
	population = city_info['population']
	mountains = city_info['nearby mountains']
	
	print(f"{city.capitalize()} is in {country.capitalize()}.")
	print(f"\t It has a population of about {population}.")
	print(f"\t The {mountains.capitalize()} mountains are nearby.")
	

	

