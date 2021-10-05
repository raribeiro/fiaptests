numOfTransactions = int(input('Informe o número de transações realizadas hoje: '))
singleTransaction = 0
totalOfTransactions = 0

for x in range(1, numOfTransactions + 1):
	singleTransaction = float(input('Informe o valor da {}º transação: '.format(x)))
	totalOfTransactions = totalOfTransactions + singleTransaction
	
	if x == numOfTransactions:
		print('O valor total gasto nas transações foi de R$%.2f sendo a média R$%.2f'% (totalOfTransactions, totalOfTransactions / numOfTransactions))
		
