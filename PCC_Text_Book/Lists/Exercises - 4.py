"""4-1: Pizzas"""
"""Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
and then use a for loop to print the name of each pizza"""
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
# Print the names of all the pizzas.
for pizza in favorite_pizzas:
	print(f'{pizza}.')
	
for pizza in favorite_pizzas:
	print(f'I really love {pizza} pizza.')

print(f'I really love pizza!')
print(f'********************************************************************************')

"""4-3: Counting to Twenty"""
"""Use a for loop to print the numbers from 1 to 20, inclusive."""
for number in range(1, 21):
	print(number)

"""4-5: Summing a Million"""
"""Make a list of the numbers from one to one million, and then use min() and max() to make
sure your list actually starts at one and ends at one million. zAlso, use the sum() function to see
how quickly Python can add a million numbers"""

num = list(range(1, 1000001))
print(f'Minimum Value --> {min(num)}')
print(f'Maximum Value --> {max(num)}')
print(f'Sum of all the numbers in the list --> {sum(num)}')
print(f'*******************************************************************************************')

"""4-7: Threes"""
"""Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list."""

my_list = list(range(3, 31, 3))
print( f'List of Multiples of 3\'s -->' )
for m in my_list:
	print(f'{m}')
print(f'********************************************************************************************')

"""4-8: Cubes"""
"""A number raised to the third power is called a cube.
For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the
cube of each integer from 1 through 10), and use a for loop to print out the value of each cube."""

cube = []
for c in range(1, 11):
	cubes = c ** 3
	cube.append(cubes)
	
for d in cube:
	print(d)
print(f'*********************************************************************************************')

"""4-9: Cube Comprehension"""
"""Use a list comprehension to generate a list of the first 10 cubes."""
list_comp = [numbers ** 3 for numbers in range(1, 11)]
for v in list_comp:
	print(v)
print(f'*********************************************************************************************')

"""4-11: My Pizzas, Your Pizzas"""
"""Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas."""
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friends_pizza = favorite_pizzas[:]

favorite_pizzas.append('meat lover\'s')
friends_pizza.append('pesto')

print(f'My favorite pizzas are:')
for f in favorite_pizzas:
	print(f'- {f}')

print(f'My friend\'s favorite pizza are:')
for g in friends_pizza:
	print(f'- {g}')
print(f'******************************************************************')

"""4-13: Buffet"""
"""A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple."""

menu_items = ('rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',)

print(f'You can choose from the following items: ')
for b in menu_items:
	print(f'- {b}')

print(f'****************************************************************')
	
try:
	menu_items[-1] = 'king crab legs'
except TypeError:
	print(f'Cannot assign value to tuple')
else:
	pass

print(f'****************************************************************')

menu_items = (
		'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
		'black cod tips', 'king crab legs',
	)

print(f'Our menu has been updated.')
for t in menu_items:
	print(f'- {t}')
print(f'*****************************************************************')









