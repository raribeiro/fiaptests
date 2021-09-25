age = int(input('Define your age: \n'))

if age > 70:
	print('invalid age')
	exit()
	
print('Set B to small risk')
print('Set M to medium risk')
print('Set A to hight risk\n')

catEnsurance = str(input(''))

if age > 16 and age < 21:
	if catEnsurance == 'B':
		print('Ensurance category 1')
	elif catEnsurance == 'M':
		print('Ensurance category 2')
	else:
		print('Ensurance category 3')
elif age > 20 and age < 25:
	if catEnsurance == 'B':
		print('Ensurance category 2')
	elif catEnsurance == 'M':
		print('Ensurance category 3')
	else:
		print('Ensurance category 4')
elif age > 24 and age < 35:
	if catEnsurance == 'B':
		print('Ensurance category 3')
	elif catEnsurance == 'M':
		print('Ensurance category 4')
	else:
		print('Ensurance category 5')
elif age > 34 and age < 65:
	if catEnsurance == 'B':
		print('Ensurance category 4')
	elif catEnsurance == 'M':
		print('Ensurance category 5')
	else:
		print('Ensurance category 6')
elif age > 64 and age < 71:
	if catEnsurance == 'B':
		print('Ensurance category 7')
	elif catEnsurance == 'M':
		print('Ensurance category 8')
	else:
		print('Ensurance category 9')
