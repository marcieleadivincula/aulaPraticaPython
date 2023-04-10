# Exercício 2 da aula ao vivo de 2022 Fase C
# # Exercício 2 de 4 da atividade prática
print('Bem-vindo a pizzaria do Marciele Almeida Adivíncula')
print('------------------------CARDÁPIO------------------------')
print('CÓDIGO | DESCRIÇÃO  | PIZZA MÉDIA(M) | PIZZA GRANDE(G) |')
print('   21  | Napolitana | R$20,00        |  R$26,00        |')
print('   22  | Margherita | R$20,00        |  R$26,00        |')
print('   23  | Calabresa  | R$25,00        |  R$32,50        |')
print('   24  | Toscana    | R$30,00        |  R$39,00        |')
print('   25  | Portuguesa | R$30,00        |  R$39,00        |')
print('--------------------------------------------------------')
acumulador = 0
while True:
    tamanho = input('Entre com o tamanho de pizza desejado(M/G): ')
    tamanho = tamanho.upper()

    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida. Pare de digitar tamanhos que não existem!')
        continue # se o usuário digitar algo inválido, volta para o começo do while

    codigo = input('Entre com o codigo da pizza desejado(21, 22, 23, 24, 25)): ')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print('Opção inválida. Pare de digitar códigos que não existem!')
        continue # se o usuário digitar algo inválido, volta para o começo do while

    if codigo == '21' and tamanho == 'M':
        print('Você escolheu a pizza Napolitana tamanho M')
        acumulador = acumulador + 20 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '21' and tamanho == 'G':
        print('Você escolheu a pizza Napolitana tamanho G')
        acumulador = acumulador + 26 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '22' and tamanho == 'M':
        print('Você escolheu a pizza Margherita tamanho M')
        acumulador = acumulador + 20 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '22' and tamanho == 'G':
        print('Você escolheu a pizza Margherita tamanho G')
        acumulador = acumulador + 26 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '23' and tamanho == 'M':
        print('Você escolheu a pizza Calabresa tamanho M')
        acumulador = acumulador + 25 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '23' and tamanho == 'G':
        print('Você escolheu a pizza Calabresa tamanho G')
        acumulador = acumulador + 32.50 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '24' and tamanho == 'M':
        print('Você escolheu a pizza Toscana tamanho M')
        acumulador = acumulador + 30 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '24' and tamanho == 'G':
        print('Você escolheu a pizza Toscana tamanho G')
        acumulador = acumulador + 39 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '25' and tamanho == 'M':
        print('Você escolheu a pizza Portuguesa tamanho M')
        acumulador = acumulador + 30 # Pegue o valor que tinha acumulador e some com 20
    elif codigo == '25' and tamanho == 'G':
        print('Você escolheu a pizza Portuguesa tamanho G')
        acumulador = acumulador + 39 # Pegue o valor que tinha acumulador e some com 20

    pedir_mais = input('Deseja pedir mais alguma pizza S ou outra tecla qualquer: ')
    pedir_mais = pedir_mais.upper()
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        break


