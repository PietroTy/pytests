from datetime import date



print('\033[1;35;46m+=\033[m'*20)

ano = int(input('Digite o ano que deseja verificar se é {}bissexto{}: '.format('\033[1;35m', '\033[m')))

print('\033[1;35;46m+=\033[m'*20)

if ano == 0: 
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

print('\033[1;35;46m+=\033[m'*20)
