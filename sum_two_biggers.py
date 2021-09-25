numOne = int(input('Set number one \n'))
numTwo = int(input('Set number two \n'))
numThree = int(input('Set number three \n'))

less = 9999999999999999999999999
summ = 0

if numOne < less:
	less = numOne
if numTwo < less:
	less = numTwo
if numThree < less:
	less = numThree
	
if numOne != less:
	summ = summ + numOne
if numTwo != less:
	summ = summ + numTwo
if numThree != less:
	summ = summ + numThree
	
print('The less number is %s'% (less))
print('The sum of two biggers is %s'% (summ))	
