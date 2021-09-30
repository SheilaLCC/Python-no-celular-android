#crie um programa que faça o computador 
#pensar em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir 
#qual foi o número escolhido pelo computador 
#o programa deverá escrever na tela se o
#usuario venceu ou perdeu
#número=int(input('De 0 a 5, digite qual número o computador escolheu?:' ))
#import random 
#n=0
#n1=1
#n2=2
#n3=3
#n4=4
#n5=5
#lista=[n,n1,n2,n3,n4,n5]
#escolhido=random.choice(lista)
#print ('O número escolhido pelo computador é:{}'.format (escolhido))
#if número==escolhido:
#    print('Parabéns você venceu!')
#else: 
#    print('Que pena, você perdeu!')

from random import randint #vai importar so número inteiro 
from time import sleep #simula como se o computador estivesse pensando 
computador=randint(0,5)
print('-=-'*16)
print('Vou pensar num numero entre 0 e 5.Tente adivinhar...')
print('-=-'*16)
jogador=int(input('Em que numero eu pensei?'))
print('Processando....') 
sleep(3)# o número corresponde a quantos segundos é a espera 
if jogador == computador:
    print('Parabens!Voce venceu!')
else: 
    print('Ganhei!Pensei no numero {} e nao no {}!'.format(computador,jogador))
    
  




