number = int(input('Informe o número e eu falo se ele faz parte da sequência de Fibonnaci: '))
startOne = 0
startTwo = 1
currentNumber = 0
successOperation = 0

for x in range(number):
	currentNumber = startOne + startTwo
	startOne = startTwo
	startTwo = currentNumber
	
	if number == currentNumber:
		successOperation = 1
		
if successOperation == 1:
	print('Ação foi bem sucedida')
else:
	print('Ação foi mal sucedida')	
