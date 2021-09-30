#crie um programa que leia quanto dinheiro 
#uma pessoa tem e calcule quantos dólares 
#ela pode comprar
# considere USD 1.00 = R$3,27
d1=float(input('Quanto dinheiro você tem na carteira R$?'))
d2=d1/3.27
print('Com R$ {:.2f}, você pode comprar US$ {:.2f} dólares.'.format (d1,d2))

