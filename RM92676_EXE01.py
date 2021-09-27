print('Simple calc of IMC \n')

height = float(input('Define your height \n'))
weight = float(input('Define your wight \n'))


imcResult = weight / (height * height)


if imcResult < 16.00:
	print('O resultado %.2f refere-se como: Baixo peso Grau III'% (imcResult))
elif imcResult >= 16.00 and imcResult < 17.00:
	print('O resultado %.2f refere-se como: Baixo peso Grau II'% (imcResult))
elif imcResult >= 17.00 and imcResult <= 18.49:
	print('O resultado %.2f refere-se como: Baixo peso Grau I'% (imcResult))
elif imcResult >= 18.50 and imcResult <= 24.99:
	print('O resultado %.2f refere-se como: Peso ideal'% (imcResult))
elif imcResult >= 25.00 and imcResult <= 29.99:
	print('O resultado %.2f refere-se como: Sobrepeso'% (imcResult))
elif imcResult >= 30.00 and imcResult <= 34.99:
	print('O resultado %.2f refere-se como: Obesidade Grau I'% (imcResult))
elif imcResult >= 35.00 and imcResult <= 39.99:
	print('O resultado %.2f refere-se como: Obesidade Grau II'% (imcResult))
elif imcResult >= 40.00:
	print('O resultado %.2f refere-se como: Obesidade Grau III'% (imcResult))
