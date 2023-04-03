# # Estrutura de repetição WHILE
# x = 1
# while x <= 5:
#     print(x)
#     x = x + 1
#
# y = 0
# while x <= 99:
#     print(y)
#     x = x + 1
#
# # Variáveis contadoras e acumuladoras
# # Contadores
# inicial = int(input('Qual valor deseja iniciar a contagem?'))
# final = int(input('Qual valor deseja finalizar a contagem?'))
# x = inicial
# while x <= final:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1
#
# # Acumuladores
# # Escreva um algoritmo que calcule a sua média de notas em determinada disciplina. Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas.
# soma = 0
# cont = 1
# while cont <= 5:
#     x = float(input('Digite a {}ª nota: '.format(cont)))
#     soma = soma + x
#     cont = cont + 1
# media = soma/5
# print('Média final: {}'.format(media))
#
# # Operadores especiais de atribuição
# c, d, e, f, g, h = 0
# c += 1 # Equivalente c = c + 1
# d -= 1 # Equivalente d = d - 1
# e *= 1 # Equivalente e = e * 1
# f /= 1 # Equivalente f = f / 1
# g **= 2 # Equivalente g = g ** 2
# h //= 2 # Equivalente h = h // 2
#
# # Outro exemplo
# soma = 0
# cont = 1
# while cont <= 5:
#     x = float(input('Digite a {}ª número: '.format(cont)))
#     soma += x
#     cont += 1
# print('Somatório: {}'.format(soma))

# # Validando dados de entrada:
# # Crie um algoritmo que receba um valor do tipo inteiro via teclado. No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos. Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor de ser solicitado.
# x = int(input('Digite um valor maior do que zero: '))
# while x <= 0:
#     x = int(input('Digite um valor maior do que zero: '))
# print('Você digitou {}. Encerrando o programa...'.format(x))

# # Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário. Encerre o algoritmo quando a palavra "sair" for digitada.
# print('Digite uma mensagem que irei repetir para você!')
# print('Para encerrar escreva "sair".')
# while True:
#     texto = input('')
#     print(texto)
#     if texto == 'sair':
#         break
# print('Encerrando o programa...')

# # Escreva um algoritmo que realize um login em um sistema. O usuário deve informar seu nome e senha.
# while True:
#     nome = input('Qual é o seu nome? ')
#     if nome != 'Lenhadorzinho':
#         continue
#     senha = input('Qual a sua senha? ')
#     if senha == 'UnInTeR':
#         break
# print('Acesso concedido.')
#
#
# # Valores Truthy e Falsey
# nome = ''
# while not nome:
#     nome = input('Digite seu nome: ')
# valor = int(input('Digite um número qualquer: '))
# if valor:
#     print('Você digitou um valor diferente de zero.')
# else:
#     print('Você digitou zero.')

# # Estrutura de repetição FOR
# for i in range(6):
#     print(i)
#
# for i in range(1, 6, 1):
#     print(i)
#
# for i in range(10, 0, -2):
#     print(i)
#
# # Escreva um algoritmo que calcule a média dos números pares de 1 até 100(1 e 100 inclusos). Implemente o laço usando "for".
# soma = 0
# qtd = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         soma += i
#         qtd += 1
#     media = soma / qtd
#     print('A média dos pares de 1 até 100 é: '.format(media))

# # Estruturas de repetição aninhadas
# # Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.
# # Vamos resolver com diferentes implementações: 2-while, 2-for e while-for
# # 2-while
# tabuada = 1
# while tabuada <= 10:
#     print('TABUADA DO {}: '.format(tabuada))
#     i = 1
#     while i <= 10:
#         print('{} X {} = {}'.format(tabuada, i, tabuada * i))
#         i += 1
#     tabuada += 1
#
# # 2-for
# for tabuada in range(1, 11, 1):
#     print('TABUADA DO {}: '.format(tabuada))
#     for tabuada in range(1, 11, 1):
#         print('{} X {} = {}'.format(tabuada, i, tabuada * i))

# while-for
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}: '.format(tabuada))
    for i in range(1, 11, 1):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1






