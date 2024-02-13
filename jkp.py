from random import randint
from time import sleep

a = 0

while a == 0:

    p1 = str (input ('Vamos jogar \033[1;35mJOKENPÔ\033[m? \nSe sim, escolha entre: \033[1;33mO\033[m, \033[1;33m[]\033[m e \033[1;33mX\033[m, se não, digite \033[1;33mSAIR\033[m: ')) .upper()
    p2 = randint(1, 3)

    while p1 not in ('O', '[]', 'X'):
        p1 = str (input ('Essa opção não existe, escolha entre: \033[1;33mO\033[m, \033[1;33m[]\033[m e \033[1;33mX\033[m. \nCaso queira sair, digite \033[1;33mSAIR\033[m: ')) .upper()

    if p1 == 'SAIR':
        a =+ 1
    
    else:

        sleep (1)
        print ('\033[1;35mJO\033[m')
        sleep (1)
        print ('\033[1;35m  KEN\033[m')
        sleep (1)
        print ('\033[1;35m     PÔ!\033[m')


        if p1 == 'O':
            p1 = 1

        elif p1 == '[]':
            p1 = 2

        elif p1 == 'X':
            p1 = 3

        if p2 == 1:
            print ('O computador escolheu: \033[1;33mO\033[m')

        elif p2 == 2:
            print ('O computador escolheu: \033[1;33m[]\033[m')

        elif p2 == 3:
            print ('O computador escolheu: \033[1;33mX\033[m')

        sleep (1)

        if p1 == 1 and p2 == 1 or p1 == 2 and p2 == 2 or p1 == 3 and p2 == 3 :
            print ('Deu empate! \033[1;33m:/\033[m')

        elif p1 == 1 and p2 == 2 or p1 == 2 and p2 == 3 or p1 == 3 and p2 == 1 :
            print ('Você perdeu! \033[1;33m:(\033[m')

        elif p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2 :
            print ('Você venceu! \033[1;33m:D\033[m')