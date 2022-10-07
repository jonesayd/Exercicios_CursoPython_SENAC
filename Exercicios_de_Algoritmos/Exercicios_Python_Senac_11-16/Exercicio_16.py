#16. Escreva um programa para calcular a redução do tempo de vida de um fumante. 
#Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. 
#Considere que um fumante perde 10 min de vida a cada cigarro. 
#Calcule quantos dias de vida um fumante perderá e exiba o total em dias.

print("----------------------------------------------------------------")
print("              TEMPO DE VIDA PERDIDO DE UM FUMANTE               ")
print("----------------------------------------------------------------")

qtd_cigar=int(input("Informe quantos cigarros sao fumados por dia: "))
qtd_anos_fum=int(input("Informe quantos anos fumando: "))

print("Considerando os", qtd_cigar, " cigarros fumados por dia durante", qtd_anos_fum, " anos")

#Encontrar a quantidade de cigarros fumados no ano
qtd_cigar_ano=qtd_cigar*365

#Encontrar a quantidade de minutos perdidos fumando
qtd_min_red=qtd_anos_fum*365*qtd_cigar*10

#Encontrar o total de tempo perdido em dias
tempo_perdido_dia=qtd_min_red/1440

#Comando 'format' usado na segunda variavel para limitar casas decimais
print("Voce fumou:", qtd_cigar_ano,  f"cigarros por ano e perdeu {tempo_perdido_dia:.2f} dias de vida!")

print("*****************************************************************")
print("         A VIDA VALE MAIS QUE UM CIGARRO! PARE DE FUMAR!         ")
print("*****************************************************************")