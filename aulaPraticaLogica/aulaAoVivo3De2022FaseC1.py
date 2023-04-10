
# Início da função volumeFeijoada()
def volumeFeijoada():
    print('------------------ Menu 1 de 3 - Volume Feijoada ------------------')
    while True:
        try:
            volumeF = int(input('Digite a quantidade desejada(ml): '))
            # Mesmo que (300 <= volumeF <= 5000)
            if (volumeF >= 300) and (volumeF <= 5000):
                return volumeF * 0.08
            else:
                print('Pare de digitar valores abaixo de 300 ou acima de 5000')
                continue #retorna para início do laço
        except ValueError:
            # Tratamento para caso o usuário digite uma letra ou número com casas decimais
            print('Pare de digitar valores não inteiros!')
# Fim da função volumeFeijoada()


# Início da função opcaoFeijoada()
def opcaoFeijoada():
    print('------------------ Menu 2 de 3 - Opção Feijoada ------------------')
    while True:
        opcaoF = input('Qual opção de feijoada deseja? \n' +
                       'b - Básica (Feijão + paiol + costelinha) \n'+
                       'p - Premium (Feijão + paiol + costelinha + partes do porco) \n'+
                       's - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n'+
                       '>>')

        opcaoF = opcaoF.lower() #Converte tudo para minúscula
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Pare de digitar opções diferentes de b/p/s')
            continue #retorna para início do laço
# Fim da função opcaoFeijoada()


# Início da função acompanhamentoFeijoada()
def acompanhamentoFeijoada():
    print('------------------ Menu 3 de 3 - Acompanhamento Feijoada ------------------')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja mais algum adicional?\n'+
                                '0 - Não deseja mais acompanhamento(encerrar pedido)\n'+
                                '1 - 200g de arroz\n'
                                '2 - 150g de farofa especial\n'+
                                '3 - 100g de couve cozida\n'+
                                '4 - 1 laranja descascada\n'
                                '>>')
        if acompanhamentoF == '0':
            return acumulador #Colocamos acumulador, pois você quer finalizar o pedido e que retorne o valor final
        elif acompanhamentoF == '1':
            acumulador = acumulador + 5
            continue #Volta para início do laço
        elif acompanhamentoF == '2':
            acumulador = acumulador + 6
            continue #Volta para início do laço
        elif acompanhamentoF == '3':
            acumulador = acumulador + 7
            continue #Volta para início do laço
        elif acompanhamentoF == '4':
            acumulador = acumulador + 3
            continue #Volta para início do laço
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3/4')
# Fim da função acompanhamentoFeijoada()

# Início do Main
print('--------------- Bem-vindo ao programa de feijoada do Renan Portela --------------')
volume = volumeFeijoada()
# print(volume)
opcao = opcaoFeijoada()
# print(opcao)
acompanhamento = acompanhamentoFeijoada()
# print(acompanhamento)
total = volume * opcao + acompanhamento
print('Total: R$ {:.2f}\nVolume: R$ {:.2f})\nOpção: R$ {:.2f}\nAcompanhamento: R$ {:.2f}'.format(total, volume, opcao, acompanhamento))