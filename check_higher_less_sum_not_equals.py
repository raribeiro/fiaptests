num1 = int(input('Enter with number 1 \n'))
num2 = int(input('Enter with number 2 \n'))
num3 = int(input('Enter with number 3 \n'))

higher = int()
less = int()
subResult = int()

if num1 == num2 or num1 == num3 or num2 == num3:
	print('Numbers are equlas')
else:
	if num1 > num2 and num1 > num3 and num2 > num3:
		less = num3
		higher = num1
	elif num1 > num2 and num1 > num3 and num3 > num2:
		less = num2
		higher = num1
	elif num2 > num1 and num2 > num3 and num3 > num1:
		less = num1
		higher = num3
	elif num3 > num1 and num3 > num2 and num1 > num2:
		less = num2
		higher = num3
	elif num3 > num1 and num3 > num2 and num2 > num1:
		less = num1
		higher = num3
	subResult = higher - less
	print(subResult)
