#crie um programa que leia o salário de 
#um funcionario e mostre seu novo salário 
#com 15% de aumento 
s=float(input ('Digite o salário,R$ '))
ns=(s*15/100)+s
print('O seu salário que era de R${:.2f}, teve um aumento de 15% e , agora é , R${:.2f} '.format (s,ns))
