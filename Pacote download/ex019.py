#um professor quer sortear um dos seus 4
#alunos para apagar o quadro.
import random
n1= str(input ('primeiro aluno :'))
n2= str(input ('segundo aluno  :'))
n3= str(input ('terceiro aluno:'))
n4= str(input ('quarto aluno:'))
lista =[n1,n2,n3,n4]
escolhido = random.choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))
