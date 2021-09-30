#crie um programa que converta uma temperatura 
#digitada em celsius para farenhit
#a regra de conversão é um formula fisica 9*c/5+32
c=float(input('Digite a temperatura em graus Celcius:' ))
f=((9*c)/5)+32
print ('A temperatura de {}°C corresponde a {}°F'.format (c,f))