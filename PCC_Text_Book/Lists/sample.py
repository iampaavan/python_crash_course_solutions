usernames_2 = ['eric', 'willie', 'admin', 'erin', 'ever']
usernames_3 = usernames_2[:]
if usernames_2:
	for username in usernames_3:
		if len(usernames_2) > 0:
			usernames_2.pop()
			print(f'Removed {username} from the list.')

print(usernames_2)
print(f'We need to find some users')
print(f'******************************************************************************************')

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000000,
    'maggie': 0,
    }

list = []
dict = {}

for key, value in favorite_numbers.items():
	list.append((key, value))

print(list)

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

Convert(list, dict)
print(dict)

for k, v in dict.items():
	print(k,v)
	
def conv(t, d1):
	d1 = dict(t)
	return d1

conv(list, dict)

for k1, v1 in dict:
	print(k1, v1)
