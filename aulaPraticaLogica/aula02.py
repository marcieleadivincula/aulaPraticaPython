# s1 = "Olá!"
# resposta = s1 + '*' * 10
# print(resposta)
#
# # Composição
# nota = 8.5
# disciplina = 'Algoritmo'
# s2 = 'Você tirou %f na disciplina de Algoritmo' % nota
# print(s2)
# # Composição com várias variáveis
# s2 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
# print(s2)
# # Composição mais moderda
# s2 = 'Você tirou {} na disciplina de {}'.format(nota, disciplina)
# print(s2)
#
# s3 = 'Lógica de Programação e Algoritmos'
# print(s3[0:6]) #vai imprimir apenas até a letra 5
# print(s3[24:34])
# print(s3[:6]) #vai imprimir tudo até o limite que eu coloquei, neste caso 6
#
# tamanho = len(s3)
# print(tamanho)

# idade = input('Qual é sua idade?')
# print(idade)
#
# nome = input('Qual é o seu nome?')
# print('Olá {}, seja bem-vindo!'.format(nome))
#
# nota = float(input('Qual é sua nota?'))
# print('Você tirou a nota {}'.format(nota))

# numero1 = int(input('Digite um número: '))
# numero2 = int(input('Digite um segundo número: '))
# soma = numero1 + numero2
# print('A soma de {} com {} é {}'.format(numero1, numero2, soma))

# # A)A somatória dos 5 primeiros números inteiros e positivos
# somatoria = 1 + 2 + 3 + 4 + 5
# # B)A média entre 23, 19 e 31
# media = (23 + 19 + 31)/3
# # C) O número de vezes que 73 cabe em 403
# divisao = 403 // 73
# # D) A sobra quando 403 é dividido por 73
# modulo = 403 % 73
# # E) 2 elevado a 10ª potência
# potencia = 2**10
# # F) O valor absoluto da diferança entre 54 e 57
# valorAbsoluto = abs(54 - 57)
# # G) O menor valor entre 34, 29 e 31
# menorValor = min(34, 29, 31)
#
# # Atribuição
# # A) Atribuir o valor inteiro 3 à variável a
# a = 3
# # B) Atribuir o valor 4 à variável b
# b = 4
# # C) Atribuir à variável c o valor da expressão a * a + b * b
# c = a*a + b*b

# # Strings
# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'
# # Utilizando os operadores + e *, crie as saídas a seguir:
# # A) 'ant bat cod'
# print(s1 + ' ' + s2 + ' ' + s3)
# # B) 'ant ant ant ant ant ant ant ant ant ant'
# print((s1 + ' ') * 10)
# # C) 'ant bat bat cod cod cod'
# print(s1 + ' ' + (s2 + ' ') * 2 + (s3 + ' ') * 3)
# # D) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# print((s1 + ' ' + s2 + ' ') * 7)
# # E) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
# print(((s2 * 2) + s3 + ' ') * 5)


# # Exercício 1
# # Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto(exercício da apostila - aula 2).
# preco = float(input('Digite o preço do produto: '))
# percentual = float(input('Digite o percentual de desconto: '))
# desconto = preco * (percentual / 100)
# valorFinal = preco - desconto
# print('O valor do desconto é {} e o preço final do produto é {}'.format(desconto, valorFinal))

# # Exercício 2
# # Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
# percurso = int(input('Digite a quantidade de km percorrido: '))
# dias = int(input('Digite a quantidade de dias que foi alugado: '))
# preco = (60.0 * dias) + (percurso * 0.15)
# print('Percurso: {} km \nDias: {}'.format(percurso, dias))
# print('Valor a ser pago: {}'.format(preco))

# Exercício 3
# Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string.
frase1 = input('Digite uma frase qualquer: ')
tam = len(frase1)
frase2 = frase1[:int(tam/2)]
frase3 = frase2[-2:] # quando colocamos negativo, significa que queremos começar a contagem de trás para frente.
print('A primeira frase é: {}'.format(frase1))
print('O tamanho do frase1 é: {}'.format(tam))
print('A segunda frase é: {}'.format(frase2))
print('Os últimos dois caracteres da segunda frase é: {}'.format(frase3))

