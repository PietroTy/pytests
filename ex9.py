num = int(input('Digite um número: '))
print('''Converta uma das bases para:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''', end=' ')
n = int(input('Sua opção: '))

if n == 1:
    print('O número {} para Binário é {} '.format(num, bin(num)[2:]))

elif n == 2:
    print('O número {} para Octal é {} '.format(num, oct(num)[2:]))

elif n == 3:
    print('O número {} para Hexadecimal é {} '.format(num, hex(num)[2:]))
