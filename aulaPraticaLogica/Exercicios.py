# # Exercício 1
# # Faça uma algoritmo que receba três valores representando os lados de uma triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# # A) Equilátero(três lados iguais); B)Isósceles(dois lados iguais); C) Escaleno(três lados diferentes).
# # Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois(exercício da apostila - aula 3).
# a = int(input('Digite o 1ª lado do triângulo: '))
# b = int(input('Digite o 2ª lado do triângulo: '))
# c = int(input('Digite o 3ª lado do triângulo: '))
# # Minha lógica
# if((a > 0) and (b > 0) and (c > 0)): #Poderia ser escrito assim: (a > 0) and (b > 0) and (c > 0) ou até assim (a > 0 and b > 0 and c > 0) ou a > 0 and b > 0 and c > 0
#     if(a + b > c) and (b + c > a) and (c + a > b):
#         if(a == b and b == c and c == a): # Se a == b and b == c, consequentemente c seria igual à a, então não precisaria fazer essa última validação
#             print('Este triângulo é equilátero, pois tem todos os lados iguais!')
#         elif a == b or b == c or c == a :
#             print('Este triângulo é isósceles, pois tem apenas dois lados iguais!')
#         elif(a != b and b != c and c != a): # Se a != b and b != c, consequentemente c seria diferente de a, então não precisaria fazer essa última validação
#             print('Este triângulo é escaleno, pois tem todos os lados diferentes!')
#         else:
#             print('Ao menos um dos valores digitados não servem para formar um triângulo!')
#     else:
#         print('Um lado não pode ser maior do que a soma dos outros dois!')
# else:
#     print('Nenhum dos lados pode ser igual à zero!')

# # Lógica do professor
# if(a > 0) and (b > 0) and (c > 0): #Poderia ser escrito assim: (a > 0) and (b > 0) and (c > 0) ou até assim (a > 0 and b > 0 and c > 0) ou a > 0 and b > 0 and c > 0
#     if(a + b > c) and (b + c > a) and (c + a > b):
#         if a != b and b != c and c != a:
#             print('Triângulo escaleno!')
#         else:
#             if(a == b and b == c and c == a):
#                 print('Triângulo equilátero!')
#             else:
#                 print('Triângulo isósceles!')
#     else:
#         print('Ao menos um dos valores digitados não servem para formar um triângulo!')
# else:
#     print('Ao menos um dos valores digitados não servem para formar um triângulo!')

# Exercício 2
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição(+), subtração(-), multiplicação(*) ou divisão(/). Exiba na tela o resultado da operação desejada(exercício da apostila - aula 3).
numero1 = float(input('Digite o 1ª número: '))
numero2 = float(input('Digite o 2ª número: '))
operacao = input('Qual operação deseja realizar: adição(+), subtração(-), multiplicação(*) ou divisão(/)? ')
if(operacao == '+'):
    print(numero1 + numero2)
elif(operacao == '-'):
    print(numero1 - numero2)
elif(operacao == '*'):
    print(numero1 * numero2)
elif(operacao == '/'):
    print(numero1 / numero2)
else:
    print('Operação inválida! Tente novamente!')

