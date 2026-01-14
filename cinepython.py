print(' --------------- Bem-vindo ao Cine Python ---------------\n ----- Preço promocional em todos os filmes por R$40 ----- ')
nome = input(' Por gentileza, qual é o seu nome? : ')
idade = int(input(' Informe sua idade? : '))
carteira = float(input(' Por gentileza, informe quanto de dinheiro possui? : R$'))
preco_ingresso = 40

if idade <= 12 or idade >= 65:
    print('--- Você possui direito a meia-entrada, seu ingresso sairá por R$20,00 ---')
    preco_ingresso = 20
else:
    print(' --- Seu ingresso sairá pelo preço promocional de R$40 --- ')

troco = carteira - preco_ingresso

if carteira == preco_ingresso:
    print(f' --- Compra realizada com sucesso, aproveite seu filme, {nome} --- ')
elif carteira < preco_ingresso:
    print(f'Valor insulficiente para o ingresso, falta R${preco_ingresso - carteira:.2f}')
elif carteira > preco_ingresso:
    print(f'Compra realizada com sucesso, seu troco é de R${troco:.2f}')
    print(f'{nome}, aproveite seu filme!')