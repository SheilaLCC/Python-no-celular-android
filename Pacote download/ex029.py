#crie um programa que leia a velocidade de 
#um carro.Se ele ultrapassar 80km/h mostre 
#uma mensagem dizendo que ele foi multado 
#a multa vai custar R$7,00 por km excedente 
velocidade=float (input ('Digite qual a velocidade:'))
if velocidade > 80:
    multa=float(velocidade-80)*7
    print('Você esta acima de 80 km e foi multado em R$ {} por km excedente. '.format(multa))
else:
    print ('Parabéns! Continue dirigindo até 80 km/h com segurança!')
    
