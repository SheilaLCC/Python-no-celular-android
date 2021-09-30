#crie um programa que leia o comprimento 
#do cateto oposto, cateto adjacente do
#triangulo retângulo e calcule a hipotenusa
from math import hypot
co=float (input ('comprimento do cateto oposto: '))
ca=float (input ('comprimento do cateto adjacente: '))
hi= hypot(co,ca)
print ('a hipotenusa vai medir {:.2f}'.format (hi))
