#crie um programa que leia a altura e a 
#largura de uma parede em metros,calcule 
#calcule a área e a quantidade de tinta
#para pintar.
#cada litro de tinta pinta uma area de 2m
h=float(input('Digite a altura da parede: '))
l=float(input('Digite a largura da parede: '))
a=h*l
t=a/2
print('A área é: {:.2f} metros quadrados. '.format (a))
print('Precisa de {:.2f} litros de tinta para pintar.'.format (t))
