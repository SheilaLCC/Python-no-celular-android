#crie um programa que pergunte a quantidade 
#de km percorridos e dias por um carro alugado 
#calcule o preço a pagar sabendo que o
#carro custa $60,00 por dia e $ 15,00 por
#km rodado 
da=int(input('Quantos dias de aluguel ?:'))
kmp=float(input('Qual a km percorrida ?:'))
pp=(kmp*0.15)+(60*da)
print('O preço a ser cobrado pelo aluguel do carro por {} dias é  de R${:.2f}'.format(da,pp))
