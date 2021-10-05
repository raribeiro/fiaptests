print('Por favor,informe a categoria selecionada: \n')

print('Para econômica digite 1')
print('Para executiva digite 2')
print('Para primeira classe digite 3')
package = int(input())

print('Por favor, informe o número de viajantes:')
numberOfPersons = int(input())

print('Por favor, informe o valor bruto do pate de viagem')
howMuch = float(input())
finalValue = float()


if package != 1 and package != 2 and package != 3:
	print('O pacote selecionado é inválido')
else:
	if package == 1:
		if numberOfPersons > 1 and numberOfPersons < 3:
			finalValue = howMuch - (howMuch * 0.03)
			print('O valor %.2f com 3%% de desconto sairá por %.2f'% (howMuch, finalValue))
		elif numberOfPersons > 2 and numberOfPersons < 4:
			finalValue = howMuch - (howMuch * 0.04)
			print('O valor %.2f com 4%% de desconto sairá por %.2f'% (howMuch, finalValue))
		else:
			finalValue = howMuch - (howMuch * 0.05)
			print('O valor %.2f com 5%% de desconto sairá por %.2f'% (howMuch, finalValue))
	elif package == 2:
		if numberOfPersons > 1 and numberOfPersons < 3:
			finalValue = howMuch - (howMuch * 0.05)
			print('O valor %.2f com 3%% de desconto sairá por %.2f'% (howMuch, finalValue))
		elif numberOfPersons > 2 and numberOfPersons < 4:
			finalValue = howMuch - (howMuch * 0.07)
			print('O valor %.2f com 4%% de desconto sairá por %.2f'% (howMuch, finalValue))
		else:
			finalValue = howMuch - (howMuch * 0.08)
			print('O valor %.2f com 5%% de desconto sairá por %.2f'% (howMuch, finalValue))
	else:
		if numberOfPersons > 1 and numberOfPersons < 3:
			finalValue = howMuch - (howMuch * 0.10)
			print('O valor %.2f com 3%% de desconto sairá por %.2f'% (howMuch, finalValue))
		elif numberOfPersons > 2 and numberOfPersons < 4:
			finalValue = howMuch - (howMuch * 0.15)
			print('O valor %.2f com 4%% de desconto sairá por %.2f'% (howMuch, finalValue))
		else:
			finalValue = howMuch - (howMuch * 0.20)
			print('O valor %.2f com 5%% de desconto sairá por %.2f'% (howMuch, finalValue))
		
