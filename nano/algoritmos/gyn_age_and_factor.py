age = int(input('Enter with age \n'))
gender = str(input('Enter with gender: M or F \n'))
factor = int(input('Enter factor 1, 2, 3, 4 or 7 \n'))
baseValue = int(input('Enter with base value \n'))
finalValue = float()
print(gender)


if gender != 'M' and gender != 'F':
	print('Invalid gender')
else:
	if gender == 'M':
		if age > 16 and age < 21:
			finalValue = baseValue * factor
			print(finalValue)
		elif age > 20 and age < 25:
			finalValue = baseValue * factor
			print(finalValue)
		elif age > 24 and age < 35:
			finalValue = baseValue * factor
			print(finalValue)
		elif age > 34 and age < 65:
			finalValue = baseValue * factor
			print(finalValue)
		elif age > 64 and age < 71:
			finalValue = baseValue * factor
			print(finalValue)
	else:
		if age > 16 and age < 21:
			finalValue = baseValue * factor * 0.8
			print(finalValue)
		elif age > 20 and age < 25:
			finalValue = baseValue * factor * 0.8
			print(finalValue)
		elif age > 24 and age < 35:
			finalValue = baseValue * factor * 0.8
			print(finalValue)
		elif age > 34 and age < 65:
			finalValue = baseValue * factor * 0.8
			print(finalValue)
		elif age > 64 and age < 71:
			finalValue = baseValue * factor * 0.8
			print(finalValue)
	
	
