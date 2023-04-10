# Importando bibliotecas: importa ao seu programa novas funções
# import math as m
# print(m.sqrt(9))  # ou print(math.sqrt(9))

# from math import sqrt
# print(sqrt(9))
#
# # Exercícios de fixação
# # Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# # a) Encontrar quantos alunos tiraram nota 7
# print(notas.count(7))
# # b) Alterar a última nota para 4
# notas[-1] = 4
# print(notas)

# # Exercício 2
# # Escreva um algoritmo que crie uma tupla com 10 palavras.
# # Encontre dentro dessa tupla as vogais de cada palavra.
# # Faça um print na tela com o nome da palavra e suas respectivas vogais.
# palavras = ('Banana', 'Laranja', 'Maçã', 'Melância', 'Jaca', 'Abacate', 'Uva', 'Morango', 'Goiaba', 'Ciriguela')
# for palavra in palavras:
#     print('\nPalavra: {}. Vogais: .'.format(palavra.upper()), end='')
#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             print(letra.upper(), end=' ')

# # Exercício 3
# # Crie um jogo de pedra, papel ou tesoura(Jokenpô). Você deverá jogar contra o computador.
# # Você irá sempre escolher uma das opções: 1 - pedra, 2 - papel, 3 - tesoura.
# # O computador irá sempre sortear um número de 1 até 3 para jogar.
# # Armazene todos os resultados em uma lista e no final apresente o vencedor.
# # Encerre o programa ao digitar zero.
# from random import randint
#
#
# def valida_int(pergunta, min, max):
#     x = int(input(pergunta))
#     while (x < min) or (x > max):
#         x = int(input(pergunta))
#     return x
#
#
# def vencedor(jogador1, jogador2):
#     global empate, v1, v2
#     if jogador1 == 1:  # pedra
#         if jogador2 == 1:  # pedra
#             empate += 1
#         elif jogador2 == 2:  # papel
#             v2 += 1
#         elif jogador2 == 3:  # tesoura
#             v1 += 1
#     elif jogador1 == 2:  # papel
#         if jogador2 == 1:  # pedra
#             v1 += 1
#         elif jogador2 == 2:  # papel
#             empate += 1
#         elif jogador2 == 3:  # tesoura
#             v2 += 1
#     elif jogador1 == 3:  # tesoura
#         if jogador2 == 1:  # pedra
#             v2 += 1
#         elif jogador2 == 2:  # papel
#             v1 += 1
#         elif jogador2 == 3:  # tesoura
#             empate += 1
#     resultados = [v1, v2, empate]
#     return resultados
#
#
# print('JOKENPÔ')
# print('1 - PEDRA')
# print('2 - PAPEL')
# print('3 - TESOURA')
#
# resultado = []
# jogadas = []
# v1 = 0
# v2 = 0
# empate = 0
#
# while True:
#     j1 = valida_int('Escolha sua jogada: ', 0, 3)
#     if not j1:  # j1 == 0
#         break
#     j2 = randint(1, 3)
#     jogadas.append([j1, j2])
#     # print(jogadas)
#     resultado = vencedor(j1, j2)
#     print(vencedor(j1, j2))
#
#     for jogada in jogadas:
#         for dado in jogada:
#             print(dado, end=' ')
#         print()
#
#
# print('Número de vitórias do jogador 1: {}'.format(resultado[0]))
# print('Número de vitórias do jogador 2: {}'.format(resultado[1]))
# print('Número de empates: {}'.format(resultado[2]))


# Exercício 4
# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
# Armazene os dados em um dicionário com listas.
# Ao encerrar o cadastro, apresente:
# a) O total de cadastros efetuados
# b) A média das idades das pessoas
# c) Uma lista de mulheres com menos de 30 anos
# d) Uma lista de homens com idade acima da média
cadastro = {'nome': [], 'sexo': [], 'ano': []}
while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    elif terminar.upper() in 'S':
        nome = input('Qual o seu nome? ')
        sexo = input('Qual o seu sexo? [M/F]')
        ano = int(input('Qual seu ano de nascimento? '))
        cadastro['nome'].append(nome)
        cadastro['sexo'].append(sexo.upper())
        cadastro['ano'].append(ano)
    else:
        print('Digite uma opção válida [S/N]')
        continue

print(cadastro)
