#crie um programa que leia uma frase pelo
#teclado e mostre,  quantas vezes aparece 
#a letra A,em que posição ela aparece a
#primeira vez e a última vez 

frase=str(input('Digite uma frase:')).upper().strip()
#quantidade=(frase.upper().count('A'))
#posicao=frase.upper().find('A')
print('A quantidade de letras A é:{}'.format(frase.count('A')))
print('A primeira letra A esta na posição:{}'.format(frase.find('A')+1))
print('A última letra A esta na posição:{}'.format(frase.rfind('A')+1))


