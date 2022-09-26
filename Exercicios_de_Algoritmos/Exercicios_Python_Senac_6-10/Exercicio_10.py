#10. Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

print("--------------------------------------------------")
print("         CÁLCULO M² E QUANTIDADE DE TINTA         ")
print("--------------------------------------------------")

larg=float(input("Insira a largura (m): "))
alt=float(input("Insira a altura (m): "))

print("--------------------------------------------------")

area=larg*alt
qtd_tinta=area/2

print("A área total a ser pintada é de: ", area, "m².")
print("Será(ão) usada(os): ", qtd_tinta, "litros de tinta.")

print("--------------------------------------------------")