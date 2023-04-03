# Aula ao Vivo de 2022 Fase C
print('Bem-vindo a loja da Marciele Almeida Adivincula')
valor_produto = float(input('Entre com o valor desejado: '))
qtd_produto = int(input('Entre com a quantidade desejada: '))
desconto_produto = 0

if qtd_produto <= 4:
    desconto_produto = 0.00
elif 5 <= qtd_produto < 20:  # Outra forma de fazer: qtd_produto >= 5 and qtd_produto < 20
    desconto_produto = 0.03
elif 5 <= qtd_produto < 20:  # Outra forma de fazer: qtd_produto >= 5 and qtd_produto < 20
    desconto_produto = 0.06
else:
    desconto_produto = 0.10

# print(desconto_produto)

total_sem_desconto = valor_produto * qtd_produto
print('O valor total sem desconto é de: R${:.2f}', format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total com desconto é de: R${:.2f}', format(total_com_desconto))

