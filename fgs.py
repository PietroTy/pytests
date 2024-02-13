from random import randint
from time import sleep

T = int (input ('Contagem regressiva quantos segundos? '))
F = int (input ('Vão ser quantos fogos? '))

for x in range (T, 0, -1):
    c = randint (1, 7)
    sleep (1)
    print ('\033[3{}m{}\033[m' .format (c, x))

for a in range (1, F+1):
    c = randint (1, 7)
    d = randint (0, 50)
    sleep (1)
    print ('\033[3{}m{} \ | / \033[m' .format (c, ' '*d))
    print ('\033[3{}m{} --+-- \033[m' .format (c, ' '*d))
    print ('\033[3{}m{} / | \ \033[m' .format (c, ' '*d))
