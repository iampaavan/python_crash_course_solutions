"""7-1: Rental Car"""
"""Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as “Let me see if I can find you a Subaru”."""

car = input(f"What kind of car would you like?")
print(f"Let me see if i can find you a {car.title()}.")
print(f"**************************************************************************")

party_size = input(f"How many people are in your dinner party tonight?")
party_size = int(party_size)

if party_size > 8:
	print(f"I'm sorry. You'll have to wait for a table.")
else:
	print(f"Your table is ready.")
print(f"*************************************************************************")

"""7-3: Multiples of Ten"""
"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

number = input(f"Give me a number, please.")
number = int(number)

if number % 10 == 0:
	print(f"{number} is a multiple of 10.")
else:
	print(f"{number} is not a multiple of 10.")
print(f'**************************************************************************')

"""7-4: Pizza Toppings"""
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value.
As they enter each topping, print a message saying you’ll add that topping to their pizza."""

prompt = f"What topping would you like on your pizza?"
prompt += f"\nEnter 'quit' when you are done."

while True:
	toppings = input(prompt)
	if toppings != 'quit':
		print(f"I'll add {toppings} to you pizza.")
	else:
		break
		
print(f'*********************************************************************************')

"""7-5: Movie Tickets"""
"""A movie theater charges different ticket prices depending on a person’s age.
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
and then tel them the cost of their movie ticket."""

ticket = f"How old are you?"
ticket += f"\n Enter 'quit' when you are done."

while True:
	user_input = input(ticket)
	if user_input == 'quit':
		break
	user_input = int(user_input)
	
	if user_input < 3:
		print(f"Your ticket is free,")
	
	elif user_input >= 3 and user_input <= 12:
		print(f"Your ticket price is 10.")
		
	else:
		print(f"Your ticket price is 15.")
	
print(f"***************************************************************************************")

"""7-8: Deli"""
"""Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and
print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move
it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made."""

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I'm working on your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)
	
print(f'*************************************************************************')
print()
print(f'Placed ordered list initially --> {sandwich_orders}')
print(f'Finished orders --> {finished_sandwiches}')
print(f'*************************************************************************')

for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich.")
print(f"*************************************************************************")

"""7-9: No Pastrami"""
"""Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami'
appears in the list at least three times. Add code near the beginning of your program
to print a message saying the deli has run out of pastrami, and then use a while loop
to remove all occurence of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches
end up in finished_sandwiches."""

sandwich_orders = [
	'pastrami', 'veggie', 'grilled cheese', 'pastrami',
	'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print(sandwich_orders)
print(f"I'm sorry, we're all out of pastrami today.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
	current_sandwiches = sandwich_orders.pop()
	print(f"I'm working on your {current_sandwiches} sandwich")
	finished_sandwiches.append(current_sandwiches)
	
print(finished_sandwiches)

for sandwiches in finished_sandwiches:
	print(f"I made a {sandwiches} sandwich.")
print(f"************************************************************************************")

"""7-10: Dream Vacation"""
"""Write a program that polls users about their dream vacation. Write a prompt similar to
If you could visit one place in the world, where would you go? Include a block of code that prints
the results of the poll."""

name_prompt = input(f"What's your name??")
place_prompt = input(f"If you could visit one place in the world, where would it be? ")
continue_prompt = input(f"Would you like to let someone else respond? (yes/no) ")

# Responses will be stored in the form {name: place}
responses = {}

while True:
	# Ask the user where they'd like to go..
	name = input(name_prompt)
	place = input(place_prompt)
	
	# Store the response
	responses[name] = place
	
	# Ask if there is anyone else responding.
	repeat = input(continue_prompt)
	if repeat != 'yes':
		break
		
# Show the results of the survey..
print(f"************************SURVEY RESULTS*********************************")
for name, place in responses.items():
	print(f"{name.title()} would like to visit {place.title()}")
	
print(f'***********************************************************************')
