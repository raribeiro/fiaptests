print('Sorteio de video game para o final do ano!\n')

play = int()
xbox = int()
nintendo = int()

#USER1#
print('Por favor, informe qual o video game selecionado para o 1° membro:\n')
print('Para o Playstation digite 1')
print('Para o XBOX digite 2')
print('Para o Nintendo digite 3\n')

selectedItem = int(input())

if selectedItem != 1 and selectedItem != 2 and selectedItem != 3:
	print('O valor informado é inválido')
else:
	if selectedItem == 1:
		play = play + 1
	elif selectedItem == 2:
		xbox = xbox + 1
	else:
		nintendo = nintendo + 1
		
	#USER2#
	print('Por favor, informe qual o video game selecionado para o 2° membro:\n')
	print('Para o Playstation digite 1')
	print('Para o XBOX digite 2')
	print('Para o Nintendo digite 3\n')

	selectedItem = int(input())

	if selectedItem != 1 and selectedItem != 2 and selectedItem != 3:
		print('O valor informado é inválido')
	else:
		if selectedItem == 1:
			play = play + 1
		elif selectedItem == 2:
			xbox = xbox + 1
		else:
			nintendo = nintendo + 1
		
		#USER3#
		print('Por favor, informe qual o video game selecionado para o 3° membro:\n')
		print('Para o Playstation digite 1')
		print('Para o XBOX digite 2')
		print('Para o Nintendo digite 3\n')

		selectedItem = int(input())

		if selectedItem != 1 and selectedItem != 2 and selectedItem != 3:
			print('O valor informado é inválido')
		else:
			if selectedItem == 1:
				play = play + 1
			elif selectedItem == 2:
				xbox = xbox + 1
			else:
				nintendo = nintendo + 1
			
			#USER4#
			print('Por favor, informe qual o video game selecionado para o 4° membro:\n')
			print('Para o Playstation digite 1')
			print('Para o XBOX digite 2')
			print('Para o Nintendo digite 3\n')

			selectedItem = int(input())

			if selectedItem != 1 and selectedItem != 2 and selectedItem != 3:
				print('O valor informado é inválido')
			else:
				if selectedItem == 1:
					play = play + 1
				elif selectedItem == 2:
					xbox = xbox + 1
				else:
					nintendo = nintendo + 1
				
				#USER5#
				print('Por favor, informe qual o video game selecionado para o 5° membro:\n')
				print('Para o Playstation digite 1')
				print('Para o XBOX digite 2')
				print('Para o Nintendo digite 3\n')

				selectedItem = int(input())

				if selectedItem != 1 and selectedItem != 2 and selectedItem != 3:
					print('O valor informado é inválido')
				else:
					if selectedItem == 1:
						play = play + 1
					elif selectedItem == 2:
						xbox = xbox + 1
					else:
						nintendo = nintendo + 1
						
print('Vamos ao campeão!!!\n')

#O algoritimo ainda não está preparado para validar empate com novas entradas
if play > xbox and play > nintendo:
	print('O campeão de votos foi o Playstation')
elif xbox > play and xbox > nintendo:
	print('O campeão de votos foi o XBOX')
else:
	print('O campeão de votos foi o Nintendo')
