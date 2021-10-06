print('Youtube Calc v1.0 \n')

print('Selecione o plano definido para o cliente')
print('Digite 1 para Basic')
print('Digite 2 para Silver')
print('Digite 3 para Gold')
print('Digite 4 para Platinum \n')

planOfClient = int(input('\n'))

if planOfClient != 1 and planOfClient != 2 and planOfClient != 3 and planOfClient != 4:
	print('Plano inválido')
else:
	valueMonth = float(input('Informe o valor/mês cobrado do cliente \n'))
	if planOfClient == 1:
		print(valueMonth*0.3)
	elif planOfClient == 2:
		print(valueMonth*0.2)
	elif planOfClient == 3:
		print(valueMonth*0.1)
	elif planOfClient == 4:
		print(valueMonth*0.05)
	 
