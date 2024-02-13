print ('~=' * 20)
print ('Super Mercadinho Pik')
print ('~=' * 20)

total = 0
comprados = 0

produtos = ('Pão', '0.99', 'Leite', '3.99', 'Sabonete', '1.99', 'Macarrão', '4.99', 'Sorvete', '9.99', 'Sanfona', '599.99', 'Pão Integra', '1399.99')

while True:

    print ('''[1] Preços
[2] Comprar
[3] Roubar
[4] Caixa
    ''')

    opcao = int ( input ('Digite seu comando: '))

    if opcao == 1:

        print (f'{"Preços":^40}')
        
        for pos in range (0, len(produtos)):

            if pos % 2 == 0:

                print (f'{produtos[pos]:.<30}', end = '')

            else:

                print (f'R$:{produtos[pos]:>7}')
    
    elif opcao == 2:

        print ('Digite o nome e quantidade dos produtos ou digite SAIR')

        while True:

            produto = input ('Produto: ') .upper()

            if produto == 'SAIR':
                break

            quantidade = int (input ('Quantidade: '))

            if produto == 'PÃO' or 'PAO':
                total += 1 * quantidade
                comprados += quantidade
            
            elif produto == 'LEITE':
                total += 4 * quantidade
                comprados += quantidade

            elif produto == 'SABONETE':
                total += 2 * quantidade
                comprados += quantidade
            
            elif produto == 'MACARRAO' or 'MACARRÃO':
                total += 5 * quantidade
                comprados += quantidade

            elif produto == 'SORVETE':
                total += 10 * quantidade
                comprados += quantidade

            elif produto == 'SANFONA':
                total += 600 * quantidade
                comprados += quantidade

            elif produto == 'PAO INTEGRAL' or 'PÃO INTEGRAL':
                total += 1400 * quantidade
                comprados += quantidade

    elif opcao == 3:

        print ('Digite o nome e quantidade dos produtos ou digite FUGIR')

        while True:

            produto = input ('Produto: ') .upper()

            if produto == 'FUGIR':
                break

            quantidade = int (input ('Quantidade: '))
            
            if produto == 'PÃO' or 'PAO':
                comprados += quantidade
            
            elif produto == 'LEITE':
                comprados += quantidade

            elif produto == 'SABONETE':
                comprados += quantidade
            
            elif produto == 'MACARRAO' or 'MACARRÃO':
                comprados += quantidade

            elif produto == 'SORVETE':
                comprados += quantidade

            elif produto == 'SANFONA':
                comprados += quantidade

            elif produto == 'PAO INTEGRAL' or 'PÃO INTEGRAL':
                comprados += quantidade

    elif opcao == 4:
        break

print ('~=' * 20)
print (f'Você gastou R${total} e levou pra casa {comprados} produtos!!!')
print ('Volte Sempre!!!')
print ('~=' * 20)

            


