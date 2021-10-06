min = int(input('Informe os minutos de sua maquina: '))
lastNumber = min
factor = min
totalFactor = min


for x in range(1, min - 1):
	factor = factor - 1
	totalFactor = totalFactor * factor
	
if totalFactor == 120:
	print('Senha descoberta com sucesso LIBERDADE%s'% (totalFactor))
else:
	print('Desculpe, mas a senha para liberação do sistema é composta de LIBERDADE + fatorial do minuto entre 1 e 60.')
	

