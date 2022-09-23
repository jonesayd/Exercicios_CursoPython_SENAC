#9. Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

print("-------------------------------------------------------------------------------")
print("|                             CONVERSOR DE MOEDA                              |")
print("-------------------------------------------------------------------------------")
print("Digite o quanto possui em reais que o programa converterá em dólar americano!")
print("-------------------------------------------------------------------------------")

reais=float(input("Digite o valor: R$ "))

print("-------------------------------------------------------------------------------")

dolar=reais/3.45

#o código usado entre as chaves é para limitar as casas decimais. Note o uso do 'f' antes da mensagem que virá e também a variável 'dolar' que vai diretamente dentro das chaves junto com a formatação de 2 casas decimais depois da vírgula, no caso, duas casas.
print(f"Você poderá comprar com a quantia digitada: {dolar:.2f} dólar(es).")
#Pode-se fazer também dessa maneira >>print("Você poderá comprar com a quantia digitada: {:.2f}".format(dolar))

print("-------------------------------------------------------------------------------")


