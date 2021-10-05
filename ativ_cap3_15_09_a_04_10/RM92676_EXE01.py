numOfFoods = int(input('Informe o número de alimentos consumidos hoje: '))
singleCalorie = 0
totalCalories = 0

for x in range(1, numOfFoods + 1):
	singleCalorie = int(input('Informe a quantidade da calorias em gramas para o alimento {}: '.format(x)))
	totalCalories = totalCalories  + singleCalorie
	
print('O total de calorias ingerida for de: {}g'.format(totalCalories))
