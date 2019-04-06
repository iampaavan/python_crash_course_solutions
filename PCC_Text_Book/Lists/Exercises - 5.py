"""5-3: Alien Colors #1"""
"""Imagine an alien was just shot down in a game. Create a variable called alien_color
and assign it a value of 'green', 'yellow', or 'red'"""

alien_color = 'green'
if alien_color == 'green':
	print(f'You earned 5 points.')

print(f'*****************************************************************************')

alien_color = 'red'
if alien_color == 'green':
	print(f'You earned 5 points.')

print(f'*****************************************************************************')

"""5-4: Alien Colors #2"""
"""Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain."""

alien_color = 'green'
if alien_color == 'green':
	print(f'You earned 5 points.')
else:
	print(f'You earned 10 points')

print(f'*****************************************************************************')

alien_color = 'yellow'
if alien_color == 'green':
	print(f'You earned 5 points.')
else:
	print(f'You earned 10 points')

print(f'*****************************************************************************')

"""5-5: Alien Colors #3"""
"""Turn your if-else chain from Exercise 5-4 into an if-elif-else chain."""

alien_color = 'red'
if alien_color == 'green':
	print(f'You earned 5 points.')
elif alien_color == 'yellow':
	print(f'You earned 10 points')
else:
	print(f'You earned 15 points')

print(f'*****************************************************************************')

alien_color = 'yellow'
if alien_color == 'green':
	print(f'You earned 5 points.')
elif alien_color == 'yellow':
	print(f'You earned 10 points')
else:
	print(f'You earned 15 points')
	
print(f'*****************************************************************************')

alien_color = 'green'
if alien_color == 'green':
	print(f'You earned 5 points.')
elif alien_color == 'yellow':
	print(f'You earned 10 points')
else:
	print(f'You earned 15 points')
	
print(f'*****************************************************************************')

"""5-6: Stages of Life"""
"""Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then"""

age = int(input(f'Enter your age: '))

if age < 2:
	print(f"You're a baby.")

elif age >=2 and age < 4:
	print(f"You're a toddler.")
	
elif age >= 4 and age < 13:
	print(f"You're a kid.")
	
elif age >= 13 and age < 20:
	print(f"You're a teenager")

elif age >= 20 and age < 65:
	print(f"You're an adult")
	
else:
	print(f"You're a senior citizen.")

print(f'*****************************************************************************')

"""5-7: Favorite Fruit"""
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
	print(f'You really like bananas')
if 'apples' in favorite_fruits:
	print(f'You really like apples.')
if 'blueberries' in favorite_fruits:
	print(f'You really like blueberries.')
if 'salmonberries' in favorite_fruits:
	print(f'You really like salmonberries')
if 'peaches' in favorite_fruits:
	print(f'You really like peaches.')
print(f'*****************************************************************')

"""5-8: Hello Admin"""
"""Make a list of five or more usernnames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user:"""

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
	if username == 'admin':
		print(f'Hello admin, would you like to see a status report?')
	else:
		print(f'Hello {username}, thank you for logging in again')

print(f'******************************************************************************************')

"""5-9: No Users"""
"""Add an if test to hello_admin.py to make sure the list of users is not empty."""

usernames_1 = ['eric', 'willie', 'admin', 'erin', 'ever']

if usernames_1:
	for username in usernames:
		if username == 'admin':
			print(f'Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {username}, thank you for logging in again')
else:
	print(f'We need to find some users.')

print(f'******************************************************************************************')

usernames_2 = ['eric', 'willie', 'admin', 'erin', 'ever']
usernames_3 = usernames_2[:]

if usernames_2:
	for username in usernames_3:
		usernames_2.remove(username)
		print(f'Removed {username} from the list.')

print(usernames_2)
print(f'We need to find some users')
print(f'******************************************************************************************')

"""5-10: Checking Usernames"""
"""Do the following to create a program that simulates how websites ensure that everyone has a unique username"""

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [cusers.lower() for cusers in current_users]
new_users_lower = [nusers.lower() for nusers in new_users]

for nul in new_users_lower:
	if nul in current_users_lower:
		print(f'Sorry {nul} has been taken. Try another username.')
	else:
		print(f'{nul} is available.')

"""5-11: Ordinal Numbers"""
numbers = list(range(1, 11))

for number in numbers:
	if number == 1:
		print(f'1st')
	elif number == 2:
		print(f'2nd')
	elif number == 3:
		print(f'3rd')
	else:
		print(f'{str(number)}th')
print(f'***********************************************************************')