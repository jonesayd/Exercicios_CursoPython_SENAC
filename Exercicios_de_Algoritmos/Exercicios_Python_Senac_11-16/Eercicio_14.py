#14. A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

print("--------------------------------------------------------")
print("              JON'S RENT A CAR - VALOR TOTAL            ")
print("--------------------------------------------------------")

km_perc=float(input("Digite a quantidade de quilometros percorridos: "))
print("--------------------------------------------------------")
diaria=float(input("Digite a quantidade de diarias: "))
print("--------------------------------------------------------")
vlr_km_perc=km_perc*0.20
vlr_diaria=diaria*90
preco_tot=vlr_km_perc+vlr_diaria

print("O custo total do aluguel e: R$", preco_tot)
print("--------------------------------------------------------")