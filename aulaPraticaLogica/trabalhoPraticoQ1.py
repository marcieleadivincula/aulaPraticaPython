# Questão 1 de 4
print('Bem-vindo à Loja da Marciele Almeida Adivíncula')
preco = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade desse produto: '))
desconto = 0
total_sem_desconto = 0
total_com_desconto = 0

if quantidade >= 1000:
    # print('Desconto de 15%')
    # Desconto de 15% para qtd = 1000 ou mais
    desconto = 0.15
elif (quantidade >= 100) and (quantidade <= 999):
    # print('Desconto de 10%')
    # Desconto de 10% para qtd de 100-999
    desconto = 0.10
elif (quantidade >= 10) and (quantidade <= 99):
    # print('Desconto de 5%')
    # Desconto de 5% para qtd de 10-99
    desconto = 0.05
else:
    # print('Sem desconto')
    # Desconto de 0% para qtd até 9
    desconto = 0.00

total_sem_desconto = preco * quantidade
print('O valor sem desconto foi: R${:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('O valor com desconto foi: R${:.2f}'.format(total_com_desconto))
# Outra forma de fazer o mesmo print
# print(f'O valor com desconto foi: R${total_com_desconto}')
valor_desconto = total_sem_desconto * desconto
print('O valor do desconto foi: R${:.2f} (desconto de {:.0f}%)'.format(valor_desconto, desconto * 100))
