from random import choice, shuffle
a = str(input('primeiro: '))
b = str(input('segundo: '))
c = str(input('terceiro: '))
list = [a, b, c]
choose = choice(list)
shuffle(list)
print('o escolhido foi {}, e a ordem é {}'.format(choose, list))