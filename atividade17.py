# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

ano=int(input("Digite um numero"))

if(ano % 4 ==0 and ano % 100 ! = 0 ) or ( ano % 400 == 0):
    print("Bissexto")
    else:
        print("Não Bissexto")



