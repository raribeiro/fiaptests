print('Validação de BPM \n')

bpm = float(input('Informe sua BPM: \n'))
age = float(input('Informe sua idade: \n'))


if age > 1 and age < 3:
	if bpm > 119 and bpm < 121:
		print('BPM dentro da normalidade')
	else:
		print('BPM anormal')
elif age > 8 and age < 18:
	if bpm > 80 and bpm < 100:
		print('BPM dentro da normalidade')
	else:
		print('BPM anormal')
elif age > 17 and age < 66:
	if bpm > 60 and bpm < 80:
		print('BPM dentro da normalidade')
	else:
		print('BPM anormal')
else:
	if bpm > 49 and bpm < 61:
		print('BPM dentro da normalidade')
	else:
		print('BPM anormal')	
