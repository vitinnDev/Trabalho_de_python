nome = input('digite seu nome: ')
disciplina = input('digite sua disciplina: ')
unota = float(input('digite a primeira nota: '))
dnota = float(input('digite a segunda nota: '))
if (unota + dnota) / 2 >= 6:
    print(f'{nome} está aprovado na disciplina {disciplina}')
else:
    print(f'{nome} está reprovado na disciplina {disciplina}')
