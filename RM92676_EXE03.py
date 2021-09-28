print('Dia escolhido por votação \n')

mon = int(input('Informe o número de votos da suganda-feira \n'))
tue = int(input('Informe o número de votos da terça-feira \n'))
wed = int(input('Informe o número de votos da quarta-feira \n'))
thu = int(input('Informe o número de votos da quinta-feira \n'))
fri = int(input('Informe o número de votos da sexta-feira \n'))


if mon > tue and mon > wed and mon > thu and mon > fri:
	print('O dia selecionado foi segunda-feira.')
elif tue > mon and tue > wed and tue > thu and tue > fri:
	print('O dia selecionado foi terça-feira.')
elif wed > mon and wed > tue and wed > thu and tue > fri:
	print('O dia selecionado foi quarta-feira.')
elif thu > mon and thu > tue and thu > wed and thu > fri:
	print('O dia selecionado foi quinta-feira.')
elif fri > mon and fri > tue and fri > wed and fri > thu:
	print('O dia selecionado foi sexta-feira.')
