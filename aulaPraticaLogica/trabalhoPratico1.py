# Bem-vindo a loja da Marciele Almeida Adivíncula
# Questão 1 de 4
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Digite a quantidade do produto: '))
desconto = 0
total_sem_desconto = 0
total_com_desconto = 0

if qtd_produto <= 9:
    # Desconto de 5% para qtd até 9
    desconto = 0.00
elif qtd_produto <= 99:
    # Desconto de 5% para qtd de 10-99
    desconto = 0.05
elif qtd_produto <= 999:
    # Desconto de 10% para qtd de 100-999
    desconto = 0.10
elif qtd_produto >= 1000:
    # Desconto de 15% para qtd = 1000 ou mais
    desconto = 0.15
else:
    print('')
