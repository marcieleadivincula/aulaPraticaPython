# TUPLA: é imutável
mochilao = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochilao)
print(mochilao[0])  # print do elemento 1 - índice 0
print(mochilao[2])  # print do elemento 3 - índice 2
print(mochilao[0:2])  # print dos elementos 1 e 2 - índice 0 e 1
print(mochilao[2:])  # print dos elementos a partir do íncide 2
print(mochilao[-1])  # print do último item

for item in mochilao:
    print('Na minha mochila tem: {}'.format(item))

tam = len(mochilao)
for i in range(0, tam, 1):
    print('Na minha mochila tem: {}'.format(mochilao[i]))

mochilao = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochilao + upgrade

print(mochilao)
print(upgrade)
print(mochila_grande)

mochila_grande_invertida = upgrade + mochilao
print(mochila_grande)
print(mochila_grande_invertida)

# Desempacotamento de parâmetros em funções
def soma(*num):  # o * significa desempacotamento
    soma = 0
    print('Tupla: {}'.format(num))
    for it in num:
        soma += it
    return soma


print('Resultado: {}\n'.format(soma(1, 2)))
print('Resultado: {}\n'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9)))


# LIST: é dinâmica, podendo ser alterado os dados e o tamanho
mochilas = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochilas)

# Alterando a lista
mochilas[2] = 'Laranja'
print('Lista: ', mochilas)

mochilas.append('Ovos')
print('Lista: ', mochilas)

mochilas.insert(1, 'Canivete')
print('Lista: ', mochilas)

# Deletando itens da lista
del mochilas[1]
print('Lista: ', mochilas)
mochilas.remove('Ovos')
print('Lista: ', mochilas)

x = [5, 7, 9, 11]
# y = x  apenas faz referência de uma lista na outra, ou seja,
# se altera uma a outra também é alterada
y = x
print(x)
print(y)

# y = x  apenas faz referência de uma lista na outra, ou seja,
# se altera uma a outra também é alterada
y[0] = 2
print(x)
print(y)

x = [5, 7, 9, 11]
y = x[:]  # dessa forma, cria uma cópia diferente, alterando apenas uma das listas
print(x)
print(y)

# Strings dentro de listas
bolsa = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(bolsa[0])

print(bolsa[0][0])
print(bolsa[2][1])

for item in bolsa:
    for letra in item:
        print(letra, end='')
    print()

for i in range(0, len(bolsa), 1):
    for j in range(0, len(bolsa[i]), 1):
        print(bolsa[i][j], end='')
    print()

comida = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
print(comida[0][0])  # retorna 'Cebola'
print(comida[0][0][0])  # retorna 'C'

# Lista dentro de listas
item = []
mercado = []
for i in range(3):  # até 3 produtos
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade do item: ')))
    item.append(float(input('Digite o valor do item: ')))
    mercado.append(item[:])
    item.clear()  # eu sempre limpo a lista, após adicionar um item, para que não duplique os itens
print(mercado)


supermarket = []
for i in range(3):  # até 3 produtos
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    supermarket.append([nome, qtd, valor])
print(supermarket)

soma = 0
print('Lista de compras: ')
print('-' * 20)
print('Item | Quantidade | Valor unitário | Total do item')
for item in supermarket:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))


# DICT: é dinâmico(podendo ser alterado); indexados por chaves(palavras-chave)
game = {
    'nome': 'Super Mário',
    'desenvolvedora': 'Nitendo',
    'ano': 1990
}

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())  # obtém somente os dados
for i in game.values():
    print(i)
print(game.keys())  # obtém somente as chaves
for i in game.keys():
    print(i)
print(game.items())  # obtém o par chave:valor
for i, j in game.items():
    print('{} = {}'.format(i, j))

# Listas com dicionários
games = []
game1 = {
    'nome': 'Super Mário',
    'videogame': 'Super Nitendo',
    'ano': 1990
}

game2 = {
    'nome': 'Zelda Ocarina of Time',
    'videogame': 'Nitendo 64',
    'ano': 1998
}

game3 = {
    'nome': 'Pokemon Yellow',
    'videogame': 'Game Boy',
    'ano': 1999
}
games = [game1, game2, game3]
print(games)


# Dicionário com listas
jogo = {}  # DICT
jogos = []  # LIST
for k in range(3):
    jogo['nome'] = input('Qual o nome do jogo? ')
    jogo['videogame'] = input('Para qual videogame ele foi lançado? ')
    jogo['ano'] = input('Qual o ano de lançamento? ')
    jogos.append(jogo.copy())
print('-' * 20)
for e in jogos:  # percorre os items da lista
    for i, j in e.items():  # percorre em cada chave:valor dentro do item
        print('O campo {} tem o valor {}.'.format(i, j))


games2 = {
    'nome': ['Super Mário', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
    'videogame': ['Super Nitendo', 'Nitendo 64', 'Game Boy'],
    'ano': [1990, 1998, 1999]
}
print(games2)

games3 = {'nome': [], 'videogame': [], 'ano': []}
for id in range(3):
    nome = input('Qual o nome do jogo? ')
    videogame = input('Para qual videogame ele foi lançado? ')
    ano = input('Qual o ano de lançamento? ')
    games3['nome'].append(nome)
    games3['videogame'].append(videogame)
    games3['ano'].append(ano)
print('-' * 20)
print(games3)

# Trabalhando com métodos em strings
s1 = list('Algoritmos')
print(s1)  # print separado
print(''.join(s1))  # print agrupado

s1[0] = 'a'
print(''.join(s1))

# Verificando caracteres
s2 = 'Lógica de Programação e Algoritmos'
# verificar se existe um padrão no início da string
s2.startswith('Lógica')  # retorna True/False

# verificar se existe um padrão no final da string
s2.endswith('Algoritmos')  # retorna True/False

# verificar se existe um padrão no final da string
s2.endswith('algoritmos')  # retorna True/False

# converter para minúscula antes de verificar se existe um padrão no final da string
s2.lower().endswith('algoritmos')  # retorna True/False

# converter para minúscula
print(s2.lower())
# converter para maiúscula
print(s2.upper())

# Contagem de caracteres:
# Conta quantas ocorrências tem da letra 'a', desconsiderando maiúsculas
s2.count('a')
# Conta quantas ocorrências tem da letra 'a', desconsiderando minúsculas
s2.count('A')
# Converte tudo para minúsculo e depois conta quantas ocorrências tem da letra 'a'
s2.lower().count('a')

s3 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s3.lower().count('mafagafinho')

# Quebrando strings
s3.split(' ')  # retorna uma lista dividida por cada espaço que existia na frase

# Substituindo strings
s3.replace('mafagafinho', 'gatinho')
s3.replace('mafagafinho', 'gatinho', 1)  # posso dizer para substituir apenas uma ocorrência


# Validação de dados em strings
s4 = 'Lógica de Programação e Algoritmos'
s5 = '42'

# Valida se tem apenas letras e números; acentos são aceitos
print(s4.isalnum())  # retorna True/False
print(s5.isalnum())  # retorna True/False

# Valida se tem apenas letras; acentos são aceitos
print(s4.isalpha())  # retorna True/False
print(s5.isalpha())  # retorna True/False

# Valida se tem apenas números
print(s4.isnumeric())  # retorna True/False
print(s5.isnumeric())  # retorna True/False
# Valida se tem apenas números; aceita também caracteres matemáticos, como frações
print(s4.isdigit())  # retorna True/False
print(s5.isdigit())  # retorna True/False

# Valida se tem apenas caracteres maiúsculos
print(s4.isupper())  # retorna True/False
print(s5.isupper())  # retorna True/False
# Valida se tem apenas caracteres minúsculos
print(s4.islower())  # retorna True/False
print(s5.islower())  # retorna True/False

s6 = 'LógicadeProgramaçãoeAlgoritmos'
# Valida se tem apenas letras; acentos são aceitos
print(s6.isalpha())  # retorna True/False

# Valida se tem apenas espaços. Inclui TAB, quebra de linha, retorno etc.
print(s4.isspace())  # retorna True/False
print(s5.isspace())  # retorna True/False
print(s6.isspace())  # retorna True/False

# Valida se tem apenas caracteres possíveis de serem impressos na tela
print(s4.isprintable())  # retorna True/False
print(s5.isprintable())  # retorna True/False
print(s6.isprintable())  # retorna True/False

