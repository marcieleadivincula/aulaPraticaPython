# Questão 4 de 4
# Início das variáveis globais
lista_peca = []
codigo_peca = 0
# Fim das variáveis globais

# Início da função cadastrar_peca()
def cadastrarPeca(codigo):
    print('Bem-vindo ao menu Cadastrar Peça')
    print('Código da peça: {}'.format(codigo))
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    preco = int(input('Entre com o PREÇO(R$) da peça: '))
    dicionario_peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'preco': preco}
    lista_peca.append(dicionario_peca.copy())
# Fim da função cadastrar_peca()


# Início da função consultar_peca()
def consultarPeca():
    print('Bem-vindo ao menu Consultar Peça')
    while True:
        try:
            opcao_consultar = input('\nEscolha a opção desejada:\n'
                                    '1 - Consultar TODAS as peças\n' +
                                    '2 - Consultar Peças por CÓDIGO\n' +
                                    '3 - Consultar Peças por FABRICANTE\n' +
                                    '4 - Retornar\n' +
                                    '>>')
            if opcao_consultar == '1':
                print('Você escolheu a opção consultar TODAS as peças')
                for peca in lista_peca:
                    print('-' * 10)
                    for key, value in peca.items():  # varer todos os conjuntos chave e valor do dicionário peça
                        print('{}: {}'.format(key, value))
                    print('-' * 10)
            elif opcao_consultar == '2':
                print('Você escolheu a opção consultar peça por CÓDIGO')
                codigo_desejado = int(input('Entre com o CÓDIGO desejado: '))
                for peca in lista_peca:
                    # o valor do campo código desse dicionário é igual ao valor desejado
                    if peca['codigo'] == codigo_desejado:
                        print('-' * 10)
                        # varer todos os conjuntos chave e valor do dicionário peça
                        for key, value in peca.items():
                            print('{}: {}'.format(key, value))
                        print('-' * 10)
            elif opcao_consultar == '3':
                print('Você escolheu a opção consultar produto(s) por FABRICANTE')
                fabricante_desejado = input('Entre com o FABRICANTE desejado: ')
                for peca in lista_peca:
                    # o valor do campo código desse dicionário é igual ao valor desejado
                    if peca['fabricante'] == fabricante_desejado:
                        print('-' * 10)
                        # varer todos os conjuntos chave e valor do dicionário peça
                        for key, value in peca.items():
                            print('{}: {}'.format(key, value))
                        print('-' * 10)
            elif opcao_consultar == '4':
                print('Você escolheu a opção RETORNAR')
                return
            else:
                print('Opção digitada inexistente!')
                print('Por favor, entre com a opção desejada novamente')
                continue
        except ValueError:
            # Tratamento para caso o usuário digite uma valor inexistente
            print('Você digitou algum valor não numérico!')
            print('Por favor, entre com a opção desejada novamente')
            continue
# Fim da função consultar_peca()


# Início da função remover_peca()
def removerPeca():
    print('Bem-vindo ao menu REMOVER peça')
    while True:
        try:
            valor_desejado = int(input('Entre com o CÓDIGO da peça que desejado remover: '))
            for peca in lista_peca:
                # verifica se o valor do campo código desse dicionário é igual ao valor desejado
                if peca['codigo'] == valor_desejado:
                    lista_peca.remove(peca)
                    print('Peça {} removida com sucesso!'.format(peca['codigo']))
                else:
                    print('Código digitado inexistente!')
                    print('Por favor, entre com o código desejado novamente')
                    continue
        except ValueError:
            # Tratamento para caso o usuário digite uma valor não numérico
            print('Você digitou algum valor não numérico!')
            print('Por favor, entre com o código desejado novamente')
            continue
# Fim da função remover_peca()


# Início do Main
print('Bem-vindo à bicicletaria da Marciele Almeida Adivíncula S.A.')
while True:
    try:
        menu = input('\nEscolha a opção desejada:\n'
                                '1 - Cadastrar Peça\n' +
                                '2 - Consultar Peça\n' +
                                '3 - Remover Peça\n' +
                                '4 - Sair\n' +
                                '>>')
        if menu == '1':
            codigo_peca += 1
            cadastrarPeca(codigo_peca)
        elif menu == '2':
            consultarPeca()
        elif menu == '3':
            removerPeca()
        elif menu == '4':
            print('Programa encerrado com sucesso...')
            break
        else:
            print('Opção digitado inexistente!')
            print('Por favor, entre com a opção desejada novamente')
            continue
    except:
        # Tratamento para caso o usuário digite uma valor inválido
        print('Você digitou algum valor inválido!')
        print('Por favor, entre com o valor desejado novamente')
        continue
# Fim do Main