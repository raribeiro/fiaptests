oddAverage = float()
oddAverageTotal = float()
evenAverage = float()
evenAverageTotal = float()
contOdd = float()
contEven = float()
win = 0
startAverage = int(input('Digite 1 para alunos ímapares ou 2 para alunos pares: '))

for x in range(1, 3):
	
	if startAverage == 1:
		for xy in range(1,26):
			print('Você está digitando as notas dos alunos ímpares. \n')
			contOdd = float(input('Informe a nota do aluno {}: '.format(xy)))
			oddAverage = oddAverage + contOdd
			
			if xy == 25:
				oddAverageTotal = oddAverage / 25
				startAverage = 2
	else:
		for xyz in range(1,26):
			print('Você está digitando as notas dos alunos pares. \n')
			contEven = float(input('Informe a nota do aluno {}: '.format(xyz)))
			evenAverage = evenAverage + contEven
			
			if xyz == 25:
				evenAverageTotal = evenAverage / 25
				startAverage = 1

if evenAverageTotal > oddAverageTotal:
	print('O os alunos pares tiveram uma média total de {} acima da média {} dos ímpares e tiveram por tanto uma maior nota'.format(evenAverageTotal, oddAverageTotal))
else:
	print('O os alunos ímpares tiveram uma média total de {} acima da média {} dos pareas e tiveram por tanto uma maior nota'.format(oddAverageTotal, evenAverageTotal))
