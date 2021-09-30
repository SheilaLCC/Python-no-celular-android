#crie um programa que leia o salário de 
#um funcionario e mostre seu aumento.
#para salário maior que 1250 calcule 10%
#para os inferiores ou iguais 15%
salário=float(input('Qual o salário atual ?'))
if salário <= 1250:  
   novo = salário + (salário * 15/100)
else:
   novo = salário + (salário * 10/100)      
print ('Seu salário de R$ {:.2f} agora é de R$ {:.2f}'.format (salário, novo))

