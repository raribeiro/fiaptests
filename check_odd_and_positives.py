numOne = int(input('Set number one \n'))
numTwo = int(input('Set number two \n'))

checkPositive = numOne > 0 and numTwo > 0
checkOdd = numOne % 2 == 1 and numTwo % 2 == 1

if checkPositive:
	print('Numbers positives')
if checkOdd:
	print('The two numbers are odd')
if checkPositive != True and checkOdd != True:
	print('Not positives and not odd')
