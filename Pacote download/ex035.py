#crie um programa que leia o comprimento 
#de 3 retas e diga se elas podem ou não 
#formar um triângulo 
r1=float(input('primeiro segmento: '))
r2=float(input('segundo segmento: '))
r3=float(input('terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2: 
    print('os segmentos acima podem formar triangulo!')
else:
    print('os segmentos acima não podem formar triangulo!')
    

