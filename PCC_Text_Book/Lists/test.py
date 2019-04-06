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
my_guest = my_guest_1[:]
for c in my_guest:
	if len(my_guest_1) > 2:
		removed = my_guest_1.pop()
		print(f'Sorry, {removed.capitalize()}. There\'s no room available')
print('***************************************************************************')
for f in my_guest_1:
	print(f'{f.capitalize()}, you are still invited for the dinner')