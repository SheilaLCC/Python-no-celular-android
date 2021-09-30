#crie um programa que leia 3 números e
#mostre qual é o maior e qual é o menor
a=int(input('Qual o primeiro número? '))
b=int(input('Qual o segundo número? '))
c=int(input('Qual o terceiro número? '))
#procurando o maior 
if a>b and a>c:   
    maior=a
if b>c and b>a:
    maior= b
if c>a and c>b:
    maior=c
#procurando o menor
if a<b and a<c:
    menor=a
if b<a and b<c:
    menor=b
if c<b and c<a:
    menor=c          
print('o maior número é {}'.format (maior))
print('o menor número é {}'.format (menor))
