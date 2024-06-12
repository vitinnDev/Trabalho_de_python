horas = int(input('digite alguma hora: '))
if horas >= 0 and horas < 12:
    print('está de manhã')
elif horas >= 12 and horas < 18:
    print('está de tarde')
else:
    print('está de noite')
