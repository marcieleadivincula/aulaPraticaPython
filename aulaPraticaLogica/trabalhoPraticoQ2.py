# Questão 2 de 4
print('Bem-vindo à lanchonete da Marciele Almeida Adivíncula')
print('------------------------CARDÁPIO-----------------------')
print('CÓDIGO  | DESCRIÇÃO                      | PREÇO(R$) |')
print('-' * 55)
print('   100  | Cachorro-Quente                |  R$9,00   |')
print('   101  | Cachorro-Quente Duplo          |  R$11,00  |')
print('   102  | X-Egg                          |  R$12,00  |')
print('   103  | X-Salada                       |  R$13,00  |')
print('   104  | X-Bacon                        |  R$14,00  |')
print('   105  | X-Tudo                         |  R$17,00  |')
print('   200  | Refrigerante Lata              |  R$5,00   |')
print('   201  | Chá Gelado                     |  R$4,00   |')
print('-' * 55)
total = 0

while True:
    preco = 0
    codigo = input('Entre com o código desejado: ')

    if codigo not in ('100', '101', '102', '103', '104', '105', '200', '201'):
        print('Opção inválida! Tente novamente!')
        continue  # se o usuário digitar algo inválido, volta para o começo do while

    if codigo == '100':
        preco = 9.00
        print('Você pediu um Cachorro-Quente no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '101':
        preco = 11.00
        print('Você pediu um Cachorro-Quente Duplo no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '102':
        preco = 12.00
        print('Você pediu um X-Egg no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '103':
        preco = 13.00
        print('Você pediu um X-Salada no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '104':
        preco = 14.00
        print('Você pediu um X-Bacon no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '105':
        preco = 17.00
        print('Você pediu um X-Tudo no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '200':
        preco = 5.00
        print('Você pediu um Refrigerante Lata no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item
    elif codigo == '201':
        preco = 4.00
        print('Você pediu um Chá Gelado no valor de R${:.2f}'.format(preco))
        total += preco  # Pega o valor total e some com o preco do item

    novamente = input('Deseja pedir mais alguma coisa?\n' +
                      '1 - Sim\n' +
                      '2 - Não\n' +
                      '>>')
    if novamente == '1':
        continue  # se o usuário digitar 1, volta para o começo do while
    else:
        print('O valor total a ser pago: R${:.2f}'.format(total))
        break  # se o usuário digitar algo diferente de 1, para a execução do código
