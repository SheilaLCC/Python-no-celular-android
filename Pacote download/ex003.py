n = input('\033[30;47mDigite algo :')
print('\033[31;46m O tipo primitivo deste valor é', type(n))
print('\033[32;45m Só tem espaços?', n.isspace())
print('\033[33;44m É numero?', n.isnumeric())
print('\033[34;43m É alfabético?', n.isalpha())
print('\033[35;42m É alfanumérico?', n.isalnum())
print('\033[36;41m Esta em maiusculas?', n.isupper())
print('\033[37;40m Esta em minúscula?', n.islower())
print('\033[7;40m Esta capitalizada?', n.istitle())
#faca um programa que leia algo pelo teclado
#mostre na tela seu tipo primitivo
#e informações utilizando o is