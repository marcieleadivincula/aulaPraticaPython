# A) O somatório de 2 com 2 é menor do que 4
print(2 + 2 < 4)
# B) O valor 7 // 3 é igual a 1 + 1
print(7 // 3 == 1 + 1)
# C) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual à 25
print(3**2 + 4**2 == 25)
# D) A soma de 2, 4 e 6 é maior do que 12
print(2 + 4 + 6 > 12)

# Continuação dos exercícios:
# A) 1387 é divisível por 19
print(1387/19)
# B) 31 é par
print(31 % 2 == 0)
# C) O menor valor entre: 34, 29 e 31 é menor do que 30
print(min(34, 29, 31) < 30)

# Exercícios de condicionais simples
# A) Se idade é maior que 60 escreva: 'Você tem direitos aos benefícios'
idade = int(input('Digite a sua idade: '))
if idade > 60:
    print('Você tem direitos aos benefícios')
# B) Se dano é maior do que 10 e escudo é igual a 0, escreva: 'Você está morto!'
dano = int(input('Digite o valor do dano: '))
escudo = int(input('Digite o valor do escudo: '))
if dano > 10 and escudo == 0:
    print('Você está morto!')
# C) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: 'Você escapou!'
if norte is True or sul is True or leste is True or oeste is True:
    # podemos simplificar a expressão acima assim: if(norte or sul or leste or oeste):
    print('Você escapou!')

# Exercícios de condicionais composta
# A) Se ano é divisível por 4, escreva: 'Pode ser um ano bissexto'. Caso contrário,
# escreva: 'Definitivamente, não é um ano bissexto'
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente, não é um ano bissexto')
# B)Se ambas as variáveis booleanas cima e baixo forem True, escreva: 'Decida-se!',
# caso contrário, escreva: 'Você escolheu um caminho!'
if cima is True and baixo is True:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
