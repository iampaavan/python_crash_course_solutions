"""7-9: No Pastrami"""
"""Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami'
appears in the list at least three times. Add code near the beginning of your program
to print a message saying the deli has run out of pastrami, and then use a while loop
to remove all occurences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches
end up in finished_sandiches."""

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

name_prompt = f"What's your name??"
place_prompt = f"If you could visit one place in the world, where would it be? "
continue_prompt = f"Would you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}
responses = dict()

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
	print(f"{name.title()} would like to visit {place.title()}.")
	
print(f'***********************************************************************')