rest = []
rest.append(['Praia', 4.2, 5.1])
rest.append(['Final', 1.2, 2.2])
rest.append(['FIAP', 10, 10.3])
rest.append(['Mineiro', 9.2, 1.8])
rest.append(['Foo 5', 1.4, 0.8])


def orderRestaurantByNote(_data):
	_data.sort(key=lambda restaurant: restaurant[1])
	_data.reverse()
	
	
	print('O filtro padrão traz uma ordenação por notas\n')
	
	for x in _data:
		print('O restaurante %s possui nota %s e distância de %skm'% (x[0], x[1], x[2]))
	
	newFilter = input('\n================\nDeseja ordenar por distância? Digite S ou N: ')
	
	if newFilter == 's':
		_data.sort(key=lambda restaurant: restaurant[2])
		
		print('Você está filtrando por distância\n')
		
		for x in _data:
			print('O restaurante %s possui nota %s e distância de %skm'% (x[0], x[1], x[2]))
		
		
orderRestaurantByNote(rest)
