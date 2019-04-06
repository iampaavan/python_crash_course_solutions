""" Store the names of a few of your friends in a list called names.
Print each person’s name by accessing each element in the list, one at a time."""

"""Exercise 3.1"""
names = ['Manju', 'Sharu', 'Thilak', 'Suuuuu']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print('**************************************')

"""Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
The text of each message should be the same, but each message should be personalized with the person’s name."""

"""Exercise 3.2"""
msg = f'Hello, {names[0]} !!!'
print(msg)

msg = f'Hello, {names[1]} !!!'
print(msg)

msg = f'Hello, {names[2]} !!!'
print(msg)

msg = f'Hello, {names[3]} !!!'
print(msg)
print('********************************************')

lists = ['Pulsar', 'Honda', 'Merc', 'Audi']
for l in lists:
	message = f'I would like to own a {l} vehicle.'
	print(message)
print('***************************************************************************')


"""If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner."""

"""Exercise 3.4"""
my_guest = ['guido van rossum', 'jack turner', 'lynn hill']
for guest in my_guest:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

"""You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite"""

"""Exercise 3.5"""

my_guest = ['guido van rossum', 'jack turner', 'lynn hill']
print(f'Original List -->')
for guest in my_guest:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

# got to know Jack Turner can't make it, so we'll call Ryan Scott for the dinner.
print(f'{my_guest[1].capitalize()} can\'t make it to the dinner')
print('***************************************************************************')

del my_guest[1]
my_guest.insert(1, 'ryan scott')
print(f'Altered List -->')
for guest in my_guest:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

"""You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner."""

"""Exercise 3.6"""
my_guest = ['guido van rossum', 'jack turner', 'lynn hill']
print(f'Original List -->')
for guest in my_guest:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

# got to know Jack Turner can't make it, so we'll call Ryan Scott for the dinner.
print(f'{my_guest[1].capitalize()} can\'t make it to the dinner')
print('***************************************************************************')

del my_guest[1]
my_guest.insert(1, 'ryan scott')
print(f'Altered List -->')
for guest in my_guest:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

print(f'We have\'t got a bigger table !!!!')
print('***************************************************************************')

new_list = ['frida kahlo', 'reinhold messner', 'elizabeth peratrovich']
print(f'New guest list -->')
for n in new_list:
	my_guest.append(n)
for p in my_guest:
	print(f'\t{p.capitalize()}, please come to dinner.')
print(f'**************************************************************************')


"""You just found out that your new dinner table won’t arrive in time for the dinner,
and you have space for only two guests"""

"""Exercise 3.7"""
my_guest_1 = []
my = ['guido van rossum', 'jack turner', 'lynn hill']
for m in my:
	my_guest_1.append(m)
print(f'Original List -->')
for guest in my_guest_1:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

# got to know Jack Turner can't make it, so we'll call Ryan Scott for the dinner.
print(f'{my_guest_1[1].capitalize()} can\'t make it to the dinner')
print('***************************************************************************')

del my_guest_1[1]
my_guest_1.insert(1, 'ryan scott')
print(f'Altered List -->')
for guest in my_guest_1:
	print(f'{guest.capitalize()}, please come to dinner.')
print('***************************************************************************')

print(f'We have got a bigger table !!!!')
print('***************************************************************************')

new_list = ['frida kahlo', 'reinhold messner', 'elizabeth peratrovich']
print(f'New guest list -->')
for n in new_list:
	my_guest_1.append(n)
for p in my_guest_1:
	print(f'\t{p.capitalize()}, please come to dinner.')
print(f'**************************************************************************')

for c in my_guest:
	if len(my_guest_1) > 2:
		removed = my_guest_1.pop()
		print(f'Sorry, {removed}. There\'s no room available')
print('***************************************************************************')
for f in my_guest_1:
	print(f'{f.capitalize()}, you are still invited for the dinner')
print('***************************************************************************')

for e in my_guest_1:
	del my_guest_1[0:]

print(my_guest_1)
print('***************************************************************************')

"""Think of at least five places in the world you’d like to visit."""
"""Exercise 3.8"""

test = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
locations = []
for l in test:
	locations.append(l)
print(f'Original List --> {locations}')
print(f'**************************************************************************')
print(f'Sorted List --> {sorted(locations)}')
print(f'**************************************************************************')
print(f'Original List --> {locations}')
print('***************************************************************************')
print(f'Reversed List --> {sorted(locations, reverse=True)}')
print(f'**************************************************************************')
print(f'Original List --> {locations}')
print('***************************************************************************')
locations.reverse()
print(f'Reverse Function --> {locations}')
print('***************************************************************************')
locations.reverse()
print(f'Back to original --> {locations}')
print(f'**************************************************************************')
locations.sort()
print(f'Using sort function --> {locations}')
print(f'**************************************************************************')
locations.sort(reverse=True)
print(f'Using sort and reverse --> {locations}')
print(f'**************************************************************************')

