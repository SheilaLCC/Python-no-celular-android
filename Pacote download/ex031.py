#crie um programa que leia a distância de 
#uma viagem em km, calcule o preço da passagem 
#cobrando R$0,50 por km até 200km e R$0,45
#para viagens mais longas
'''distância=float(input('Digite quantos kms tem a viagem: '))
if distância <= 200:
    preço = distância * 0.50
    print(' O preço da viagem é R$ {:.2f}'.format (preço))
else:
    preço = distância * 0.45
    print ('O preço da viagem é R$ {:.2f}'.format (preço))
print ('Boa viagem!') '''

distância=float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}km.'.format (distância))
preço =distância *0.50 if distância <=200 else distância * 0.45
print ('E o preço da sua viagem será de R${:.2f}'.format (preço))
