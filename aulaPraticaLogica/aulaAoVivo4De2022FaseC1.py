# Início das variáveis globais
lista_produto = []
codigo_produto = 0
# Fim das variáveis globais


# Início da função cadastrar_produto()
def cadastrar_produto(codigo):
    print('Bem-vindo ao menu Cadastrar Produto')
    print('Código do produto: {}'.format(codigo))
    nome = input('Entre com o NOME do produto: ')
    fabricante = input('Entre com o FABRICANTE do produto: ')
    preco = int(input('Entre com o PREÇO(R$) do produto: '))
    dicionario_produto = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'preco': preco}
    lista_produto.append(dicionario_produto.copy())
# Fim da função cadastrar_produto()


# Início da função consultar_produto()
def consultar_produto():
    print('Bem-vindo ao menu Consultar Produto')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n'
                                '1 - Consultar TODOS os produtos\n' +
                                '2 - Consultar produto por CÓDIGO\n' +
                                '3 - Consultar produto por FABRICANTE\n' +
                                '4 - Retornar\n' +
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar TODOS os produtos')
            for produto in lista_produto:
                print('-' * 10)
                for key, value in produto.items():  # varer todos os conjuntos chave e valor do dicionário produto
                    print('{}: {}'.format(key, value))
                print('-' * 10)
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar produto por CÓDIGO')
            codigo_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for produto in lista_produto:
                # o valor do campo código desse dicionário é igual ao valor desejado
                if produto['codigo'] == codigo_desejado:
                    print('-' * 10)
                    for key, value in produto.items():  # varer todos os conjuntos chave e valor do dicionário produto
                        print('{}: {}'.format(key, value))
                    print('-' * 10)
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar produto(s) por FABRICANTE')
            fabricante_desejado = input('Entre com o FABRICANTE desejado: ')
            for produto in lista_produto:
                # o valor do campo código desse dicionário é igual ao valor desejado
                if produto['fabricante'] == fabricante_desejado:
                    print('-' * 10)
                    for key, value in produto.items():  # varer todos os conjuntos chave e valor do dicionário produto
                        print('{}: {}'.format(key, value))
                    print('-' * 10)
        elif opcao_consultar == '4':
            print('Você escolheu a opção RETORNAR')
            return
        else:
            print('Opção inválida! Tente novamente!')
            continue
# Fim da função consultar_produto()


# Início da função remover_produto()
def remover_produto():
    print('Bem-vindo ao menu REMOVER produto')
    valor_desejado = int(input('Entre com o CÓDIGO do produto que desejado remover: '))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual ao valor desejado
            lista_produto.remove(produto)
            print('Produto {} removido com sucesso!'.format(produto))
        else:
            print('Código digitado inexistente! Tente novamente!')
            continue
# Fim da função remover_produto()


# Início do Main
print('Bem-vindo à mercearia do Renan Portela Jorge')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'
                            '1 - Cadastrar Produto\n' +
                            '2 - Consultar Produto\n' +
                            '3 - Remover Produto\n' +
                            '4 - Sair\n' +
                            '>>')
    if opcao_principal == '1':
        codigo_produto = codigo_produto + 1
        cadastrar_produto(codigo_produto)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        print('Programa encerrado com sucesso...')
        break
    else:
        print('Opção inválida! Tente novamente!')
        continue
# Fim do Main
