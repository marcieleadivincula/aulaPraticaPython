# # 02 de abril de 2023
# # Função sem parâmetros
# def realce():
#     #corpo da função
#     print('|', '_' * 10, '|')
#     print('|', '_' * 10, '|')
#
# #programa principal
# realce()
# print('      MENU')
# realce()
from typing import TextIO


# # Função com parâmetros
# def realce(s1):
#     print('|', '_' * 10, '|')
#     print('|', '_' * 10, '|')
#     print(s1)
#     print('|', '_' * 10, '|')
#     print('|', '_' * 10, '|')
#
# realce('      Vini')

# def sub2(x, y):
#     res = x - y
#     print(res)
#
#
# sub2(5, 7)
# sub2(7, 2)
# sub2(y = 7, x = 5) # explicitando qual valor vai receber

# def soma3(x, y, z):
#     res = x + y + z
#     print(res)
#
# soma3(5, 2, 3)
#
# def soma4(x = 0, y = 0, z = 0):
#     res = x + y + z
#     print(res)
#
# soma4(1, 2, 3)
# soma4(1, 2) # z foi omitido
# soma4(1) #y e z foram omitidos
# soma4() #x, y e z foram omitidos


# # Exercício: Escreva uma rotina que crie uma borda ao redor de uma palavra para destacá-la como sendo um título.
# # A rotina deve receber como parâmetro a palavra a ser destacada.
# # O tamanho da caixa de texto deverá ser adaptável de acordo com o tamanho da palavra.
# def borda(palavra):
#     tamanho = len(palavra)
#     # Só imprimi caso exista algum caractere
#     if tamanho:
#         print('+', '-' * tamanho, '+')
#         print('|', palavra, '|')
#         print('+', '-' * tamanho, '+')
#
# borda('maria')
# borda('pneumoultramicroscopicossilicovulcanoconiose')
# borda('Olá, mundo!')
# borda('paralelepípedo')
# borda('Lógica de Programação e Algoritmos')


# # Escopo de variáveis
# def comida():
#     print(ovos)
#
# ovos = 12 # variável global
# comida()
#
# def comida2():
#     ovos = 12 # variável local de comida2
#     bacon()
#     print(ovos)
#
# def bacon():
#     ovos = 6 # variável local de bacon
#
# comida2()

# def comida3():
#     ovos = 'Variável local de comida'
#     print(ovos)
#
# def bacon():
#     ovos = 'Variável local de bacon'
#     print(ovos)
#     comida3()
#     print(ovos)
#
# ovos = 'Variável global'
# bacon()
# print(ovos)

# def food():
#     global ovos # Usando essa instrução, alteramos o valor da variável global
#     ovos = 'comida'
#
# #programa principal
# ovos = 'global'
# food()
# print(ovos)

# # Retorno de valores de funções
# def soma3(x = 0, y = 0, z = 0):
#     res = x + y + z
#     return res
#
# retornado = soma3(1, 2, 3)
# print('O valor retornado é: {}'.format(retornado))
#
# retornado1 = soma3(1, 2, 3)
# retornado2 = soma3(1, 2)
# retornado3 = soma3()
# print('Somatórios: {}, {} e {}.'.format(retornado1, retornado2, retornado3))
#

# # Exercício 1: Escreva uma função para validar uma string.
# Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo,
# e falso, caso contrário(elaborado com base em Menezes, s.d.).
# def valida_string(pergunta, min, max):
#     s1 = input(pergunta)
#     tam = len(s1)
#     while ((tam < min) or (tam > max)):
#         s1 = input(pergunta)
#         tam = len(s1)
#     return s1
#
# x = valida_string('Digite uma string: ', 10, 20)
# print('Você digitou a string: {}. \nDado válido. Encerrando o programa...'.format(x))

# # Recursos avançados com funções
# # Exceções comuns em Python: ZeroDivisionError, ValueError, IndexError
# while True:
#     try:
#         x = int(input('Por favor, digite um número: '))
#         break
#     except ValueError:
#         print('Oops! Número inválido! Tente novamente!')
#
# def div():
#     try:
#         num1 = int(input('Digite um número: '))
#         num2 = int(input('Digite um número: '))
#         res = num1 / num2
#     except ZeroDivisionError:
#         print('Oops! Erro de divisão por zero...')
#     except:
#         print('Algo de errado aconteceu...')
#     else:
#         return res
#     finally:
#         print('Executará sempre!')
#
# print(div())

# # Funcção como parâmetro de outra função
# def imprime_com_condicao(num, fcond):
#     if fcond(num):
#         print(num)
#
# def par(x):
#     return x % 2 == 0
# def impar(x):
#     return not par(x)
#
# imprime_com_condicao(5, par)
# imprime_com_condicao(5, impar)

# # Função lambda
# res = lambda x: x * x
# print(res(3))
#
# soma = lambda x, y: x + y
# print(soma(3, 5))
#

# # Aula 05.2
# # Interactive Help
# def soma(x=0, y=0, z=0):
#     """
#     Função que soma até três valores inteiro
#     :param x: valor inteiro opcional
#     :param y: valor inteiro opcional
#     :param z: valor inteiro opcional
#     :return: soma inteira
#     """
#     return x+y+z
#
# print(soma(3, 2))
# help(soma)
#
# # Exercício 1: Escreva uma função que calcule o fatorial de um número recebido
# como parâmetro e retorne o seu resultado.
# # Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos.
# # Crie o help da sua função(exercício da apostila - aula 5).
# def valida_int(pergunta, min, max):
#     x = int(input(pergunta))
#     while(x < min) or (x > max):
#         x = int(input(pergunta))
#     return x
#
#
# def fatorial(num):
#     """
#     Calcula a fatorial
#     :param num: número inteiro qualquer
#     :return: retorna a fatorial de um número inteiro
#     """
#     fat = 1
#     if num == 0:
#         return fat
#     for i in range(1, num+1, 1):
#         fat *= i
#     return fat
#
#
# y = valida_int('Digite uma valor para calcular a fatorial: ', 0, 99999)
# print('{}! = {}'.format(y, fatorial(y)))
# help(fatorial)


# Exercício 2: Suponha que você é um colecionador de jogos de videogame.
# Escreva um algoritmo que permite cadastrar esses jogos informando o nome e a qual videogame ele pertence.
# Para isso, crie um menu de opções contendo: casdastrar novo item, listar tudo que foi cadastrado e sair.
# Para resolver esse exercício, crie pelo menos uma função para cada item do menu.
# Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados.
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while(x < min) or (x > max):
        x = int(input(pergunta))
    return x


def cria_arquivo(nome_arquivo):
    try:
        arq = open(nome_arquivo, 'wt+')
        arq.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nome_arquivo))

def existe_arquivo(nome_arquivo):
    try:
        arq = open(nome_arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lista_cadastrados(nome_arquivo):
    a = TextIO
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('Arquivo lido com sucesso!')
        print(a.read())
    finally:
        a.close()


def cadastra_jogo(narquivo, njogo, nvideogame):
    arqv = TextIO
    try:
        arqv = open(narquivo, 'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        tam = len(njogo + nvideogame)
        print('Arquivo aberto com sucesso!')
        arqv.write('*' * tam)
        print(tam)
        arqv.write('\n+ {} | {} +\n'.format(njogo, nvideogame))
        arqv.write('*' * tam)
        print(tam)
    finally:
        arqv.close()


arquivo = 'game.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente!')
    cria_arquivo(arquivo)

while True:
    print('MENU')
    print('-' * 10)
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')
    print('-' * 10)

    opcao = valida_int('Escolha a opção desejada: ', 1, 3)
    if opcao == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nome_jogo = input('Nome do jogo: ')
        nome_videogame = input('Nome do videogame: ')
        cadastra_jogo(arquivo, nome_jogo, nome_videogame)
    elif opcao == 2:
        print('Opção de listar cadastros selecionada...\n')
        lista_cadastrados(arquivo)
    elif opcao == 3:
        print('Encerrando o programa...')
        break
