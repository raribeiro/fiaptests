numOne = int(input('Set number one \n'))
numTwo = int(input('Set number two \n'))
operation = str();

print('\nUse * for multiplication')
print('Use + for sum')
print('use - for subtraction')
print('use / for division')

operation = input('')

if operation != '*' and operation != '+' and operation != '-' and operation != '/':
	print('Invalid operation');
elif operation == '*':
	print(numOne * numTwo)
elif operation == '+':
	print(numOne + numTwo)
elif operation == '-':
	print(numOne - numTwo)
elif operation == '/':
	if numTwo == 0:
		print('Division by 0 is not possible!')
	else:
		print(numOne / numTwo)
