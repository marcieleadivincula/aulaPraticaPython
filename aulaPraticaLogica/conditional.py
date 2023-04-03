# x = int(input('Digite um valor inteiro: '))
# y = int(input('Digite um segundo valor inteiro: '))
# if(x > y):
#     print('O primeiro valor é maior que o segundo!')
# else:
#     print('O segundo valor é maior que o primeiro!')
#
# a = int(input('Digite um valor inteiro: '))
# if (a % 2 == 0):
#     print('O número é par!')
# else:
#     print('O número é ímpar!')
#
# # Expressões lógicas e álgebra booleana
# #not
# b = True
# c = False
# print(not b)
# print(not c)
#
# #and (se ao menos uma das entradas for false, sempre retornará false)
# d = True
# e = False
# print(d and e)
#
# # or (se ao menos uma das entradas for verdadeira, sempre retornará verdadeiro)
# f = True
# g = False
# print(f or g)

# # Expressões lógicas - EXEMPLOS
# x = 10
# y = 1
# z = 5.5
#
# res = not x > y
# print(res)
#
# res = x > y and z == y
# print(res)

# # Exercício
# # Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando. Assuma que a média para aprovação é a partir de 7 e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em casa matéria e informe, na tela, se ele passou de ano ou não.
# nota1 = float(input('Digite a nota da 1ª matéria: '))
# nota2 = float(input('Digite a nota da 2ª matéria: '))
# nota3 = float(input('Digite a nota da 3ª matéria: '))
# if(nota1 >= 7 and nota2 >= 7 and nota3 >= 7):
#     print('O aluno está aprovado!')
# else:
#     print('O aluno está reprovado!')

# #Condicionais aninhadas - Exercício
# # Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana. Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela. Considere que uma maçã custa R$2,30, uma laranja R$3,60 e uma banana R$1,85.
# print('Escolha o que deseja comprar: ')
# print('1 - Maçã')
# print('2 - Laranja')
# print('3 - Banana')
# produto = int(input('Qual sua escolha? '))
# qtd = int(input('Quantas unidades deseja? '))
# if(produto == 1):
#     pagar = qtd * 2.3
#     print('Você comprou {} maçãs. Total à pagar: {}'.format(qtd, pagar))
# else:
#     if(produto == 2):
#      pagar = qtd * 3.6
#      print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
#     else:
#         if(produto == 3):
#             pagar = qtd * 1.85
#             print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
#         else:
#             print('Produto inexistente!')

#Condicionais de múltipla escolha - Exercício
print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades deseja? '))
if(produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maçãs. Total à pagar: {}'.format(qtd, pagar))
elif(produto == 2):
     pagar = qtd * 3.6
     print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
elif(produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
else:
    print('Produto inexistente!')

# Exercício 2
# Escreva um algoritmo que lê um nome e uma idade.
# Caso o nome digitado seja Vinicius, escreva isso na tela;
# Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100 anos, informe que esta pessoa possivelmente não existe.
nome = input('Qual  seu nome? ')
idade = int(input('Qual é a sua idade? '))
if(nome == 'Vinicius!'):
    print('Olá, Vinicius!')
elif(idade < 18):
    print('Você não é o Vinicius! E é menor de idade!')
elif(idade > 100):
    print('Diferente de você, o Vinicius não é imortal!')