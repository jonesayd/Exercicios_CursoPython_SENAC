#13. Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento. 

print("------------------------------------------------")
print("|                 NOVO SALARIO                 |")
print("------------------------------------------------")

salario=float(input("Digite o valor do salario: "))
aumento=(salario*15)/100
salario_atual=salario+aumento

print("\n*************************************************")
print("Parabens, voce recebeu um aumento no seu salario!")
print("*************************************************\n")
print("O seu novo salario e: R$ ", salario_atual)
print("-------------------------------------------------")