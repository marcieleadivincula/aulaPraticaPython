# Questão 3 de 4
# Início da função dimensoes_objeto()
def dimensoes_objeto():
    # Valida as dimensões do objeto:
    while True:
        try:
            comprimento = int(input('Digite o comprimento do objeto(em cm): '))
            largura = int(input('Digite a largura do objeto(em cm): '))
            altura = int(input('Digite a altura do objeto(em cm): '))
            volume = comprimento * largura * altura

            if volume < 1000:
                print('O volume do objeto(em cm3) é: {}'.format(volume))
                return 10.0
            elif 1000 <= volume < 10000:
                print('O volume do objeto(em cm3) é: {}'.format(volume))
                return 20.0
            elif 10000 <= volume < 30000:
                print('O volume do objeto(em cm3) é: {}'.format(volume))
                return 30.0
            elif 30000 <= volume < 100000:
                print('O volume do objeto(em cm3) é: {}'.format(volume))
                return 50.0
            elif volume >= 100000:
                # Volume maior e igual à 100000 não é aceito
                print('O volume do objeto(em cm3) é: {}'.format(volume))
                print('Não aceitamos objetos com dimensões tão grandes!')
                print('Por favor, entre com as dimensões desejadas novamente!')
                continue
        except ValueError:
            # Tratamento para caso o usuário digite uma valor não numérico
            print('Você digitou alguma dimensão do objeto com valor não numérico!')
            print('Por favor, entre com as dimensões desejadas novamente!')
            continue
# Fim da função dimensoes_objeto()


# Início da função peso_objeto()
def peso_objeto():
    # Valida o peso do objeto:
    while True:
        try:
            peso_digitado = int(input('Digite o peso do objeto(em kg): '))
            if peso_digitado <= 0.1:
                multpeso = 1.0
                print('PESO: {} * MULTIPLICADOR: {} = {}'.format(peso_digitado, multpeso, peso_digitado * multpeso))
                return multpeso
            elif 0.1 <= peso_digitado < 1:
                multpeso = 1.5
                print('PESO: {} * MULTIPLICADOR: {} = {}'.format(peso_digitado, multpeso, peso_digitado * multpeso))
                return multpeso
            elif 1 <= peso_digitado < 10:
                multpeso = 2.0
                print('PESO: {} * MULTIPLICADOR: {} = {}'.format(peso_digitado, multpeso, peso_digitado * multpeso))
                return multpeso
            elif 10 <= peso_digitado < 30:
                multpeso = 3.0
                print('PESO: {} * MULTIPLICADOR: {} = {}'.format(peso_digitado, multpeso, peso_digitado * multpeso))
                return multpeso
            elif peso >= 30:
                # Peso maior e igual à 30 não é aceito
                print('Não aceitamos objetos tão pesados!')
                print('Por favor, entre com o peso desejado novamente!')
                continue
        except ValueError:
            # Tratamento para caso o usuário digite uma valor não numérico
            print('Você digitou algum peso do objeto com valor não numérico!')
            print('Por favor, entre com o peso desejado novamente!')
            continue
# Fim da função peso_objeto()


# Início da função rota_objeto()
def rota_objeto():
    # Verifica a rota selecionada:
    while True:
        try:
            rota_selecionada = input('Selecione a rota:\n' +
                         'BR - De Brasília para Rio de Janeiro\n' +
                         'BS - De Brasília para São Paulo\n' +
                         'RB - De Rio de Janeiro para Brasília\n' +
                         'RS - De Rio de Janeiro para São Paulo\n' +
                         'SR - De São Paulo para Rio de Janeiro\n' +
                         'SB - De São Paulo para Brasília\n' +
                         '>>')
            if rota_selecionada.upper() == 'BR':
                multrota = 1.5
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            elif rota_selecionada.upper() == 'BS':
                multrota = 1.2
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            elif rota_selecionada.upper() == 'RB':
                multrota = 1.5
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            elif rota_selecionada == 'RS':
                multrota = 1.0
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            elif rota_selecionada.upper() == 'SR':
                multrota = 1.0
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            elif rota_selecionada.upper() == 'SB':
                multrota = 1.2
                print('O multiplicador da rota {} é {}'.format(rota_selecionada, multrota))
                return multrota
            else:
                print('Você digitou uma rota que não existe!')
                print('Por favor, entre com a rota desejada novamente')
                continue
        except ValueError:
            # Tratamento para caso o usuário digite uma valor numérico
            print('Você digitou uma rota que não existe')
            print('Por favor, entre com a rota desejada novamente')
            continue
# Fim da função rota_objeto()


# Início do programa principal
print('Bem-vindo à Companhia Logística da Marciele Almeida Adivíncula S.A.')
dimensoes = dimensoes_objeto()
# print(dimensoes_objeto)
peso = peso_objeto()
# print(peso_objeto)
rota = rota_objeto()
# print(rota_objeto)
total = dimensoes * peso * rota
print('Total a pagar(R$): {:.2f} (dimensões: {:.1f} * peso: {:.1f} * rota: {:.1f})'.format(total, dimensoes, peso, rota))
# Fim do programa principal
