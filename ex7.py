vel = float (input ('qual a vel atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print("voce vai ter que pagar {:.2f}" .format(multa))

else: print ('entao ta')