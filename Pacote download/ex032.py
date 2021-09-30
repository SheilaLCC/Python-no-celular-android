#crie um programa que leia um ano e mostre 
#se ele é bissexto 
from datetime import date 
ano=int(input('Qual o ano com 4 digitos? Coloque 0 para analisar ano atual: '))
if ano==0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Ano bissexto!'.format(ano))
else:
    print('O ano {} não é Ano bissexto!'.format(ano))
