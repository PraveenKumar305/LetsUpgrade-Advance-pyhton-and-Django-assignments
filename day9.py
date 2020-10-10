import random 
 
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$^&%*'
number = input('Number of passwords? - ')
number = int(number)

length = input('password length? - ')
length = int(length)

for p in range(number):
	password = ''
	for c in range(length):
		password += random.choice(chars)
	print(password)
