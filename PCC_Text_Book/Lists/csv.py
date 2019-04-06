import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert',
               'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth',
               'Laura', 'Jennifer', 'Maria', 'Paavan', 'Akshay', 'Hemal', 'Satish', 'Virat', 'Kedar', 'Shikar', 'Rohit',
               'KL', 'MS', 'Mohammed', 'Abcd', 'ecfgt', 'Ishanth', 'PL', 'Glenn', 'Steve', 'David', 'IPL', 'Karun', 'Bhushan',
               'Bhuavan', 'Varun', 'Aishu', 'Shobha', 'Manju', 'Sharu', 'Thilak', 'Macha', 'Asvini', 'Suuu', 'Ashwini', 'Shobana']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson',
              'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
              'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Gopala', 'Murgod', 'KumarGadhiya', 'Anabalagan',
              'asdasjkkj', 'asdgagh', 'ygfa', 'adugf', 'agyuyaugfr', 'surwihufd', 'asdugas', 'euiewiu', 'asgdjas', 'iuerote', 'plkdfond',
              'twuejczb', 'dijlghijgj']

passwords = ['Admin@11111', 'Admin@22222', 'Admin@33333', 'Admin@44444', 'Admin@55555', 'Admin@66666', 'Admin@77777', 'Admin@88888',
             'Admin@99999', 'Admin@00000', 'Admin@12345', 'Admin@12344', 'Admin@12355', 'Admin@13141', 'Admin@52415', 'Admin@01010',
             'Admin@15915', 'Admin@95195', 'Admin@74125', 'Admin@85256', 'Admin@78965', 'Admin@19515', 'Admin@75369', 'Admin@75487',
             'Admin@03030', 'Admin@04040', 'Admin@05050', 'Admin@06060', 'Admin@07070', 'Admin@08080', 'Admin@09090', 'Admin@57578',
             'Admin@75874655', 'Admin@355365', 'Admin@6845451', 'Admin@65453', 'Admin@65453', 'Admin@08080', 'Admin@09090', 'Admin@57578']


with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\users.txt', 'w',
           encoding="utf-8") as file_handler:
	
	for num in range(2000):
		first = random.choice(first_names)
		last = random.choice(last_names)
		email = first.lower() + last.lower() + '@gmail.com'
		password = random.choice(passwords)
		file_handler.write(f'{password}\n')
		print()
