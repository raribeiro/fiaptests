numOne = int(input('Set number one \n'))
numTwo = int(input('Set number two \n'))

calNumOne = numOne % 2 == 0 and numTwo % 2 == 0
calNumTwo = numOne % 2 != 0 and numTwo % 2 != 0

if calNumOne:
	print('All numbers even.')
elif calNumTwo:
	print('All numbers odd.')
else:
	print('Numbers even and odd.')
