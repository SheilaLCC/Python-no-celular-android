#crie um programa que leia o nome completo 
#de uma pessoa e mostre o nome com todas 
#as letras maiusculas,minúsculas,total 
#de letras sem espaços,quantas letras tem
#o primeiro nome

nome=str(input('Digite seu nome completo :')).strip()
#dividido=nome.split()
print('Analisando seu nome completo...')
print('Seu nome maiusculo é {}'.format (nome.upper()))
print('Seu nome minúsculo é {}'.format (nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))