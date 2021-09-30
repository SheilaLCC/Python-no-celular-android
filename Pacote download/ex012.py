#crie um programa que leia o preço de um
#produto e mostre seu novo preço com 5%
#de desconto 
p=float(input('Digite o preço do produto:R$ '))
pn=p-(p*5/100)
print ('O novo preço com desconto de 5% é:R$ {:.2f}'.format (pn))
