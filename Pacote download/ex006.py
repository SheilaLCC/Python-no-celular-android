#crie um algoritmo que leia um número e
#mostre o seu dobro, triplo e a raiz 
#quadrada
n=int(input('\033[7;40m Digite um número : \033[m' ))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de \033[31;40m{}\033[m é \033[31;40m{}\033[m'.format (n,d))
print('O triplo de \033[m{} é {}\033[m'.format (n,t))
print('A raiz quadrada de \033[m{} é {:.2f}\033[m'.format (n,r))
