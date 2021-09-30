#crie um programa que leia um ângulo qq
#mostre na tela o valor do seno,cosseno e
#tangente desse ângulo 
import math
ângulo=float(input ('Digite o ângulo que vc deseja:'))
seno=math.sin(math.radians(ângulo))
print ('O ângulo de {} tem o seno de {:.2f}'.format (ângulo, seno))
cosseno=math.cos(math.radians (ângulo))
print ('O ângulo de {} tem o cosseno de {:.2f}'.format (ângulo,  cosseno))
tangente=math.tan(math.radians (ângulo))
print ('O ângulo de {} tem a tangente de {:.2f}'.format (ângulo, tangente))