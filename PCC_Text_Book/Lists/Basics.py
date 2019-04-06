bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print('*************************************************')
print(bicycle[0])
print('*************************************************')
print(bicycle[0].capitalize())
print('*************************************************')
print(bicycle[0].title())
print('*************************************************')
print(bicycle[1])
print('*************************************************')
print(bicycle[3])
print('*************************************************')
print(bicycle[-1])
print('*************************************************')
message = f'My first bicycle was a {bicycle[0].capitalize()}.'
print(message)
print('*************************************************')

favorite_numbers = {
	'mandy': 42,
	'micah': 23,
	'gus': 7,
	'hank': 1000000,
	'maggie': 0,
}

list = []
d = {}

for key, value in favorite_numbers.items():
	list.append((key, value))

print(list)


for k, v in favorite_numbers.items():
	print(k, v)


def conv(t, p):
	p = dict(t)
	return p


conv(list, d)

for k1, v1 in d:
	print(k1, v1)

