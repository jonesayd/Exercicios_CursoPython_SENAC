#8. Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

print("-------------------------------------------------------------------------------")
print("|                          CÁLCULO EM OUTRAS MEDIDAS                          |")
print("-------------------------------------------------------------------------------")
print(">Escolha uma distância em metros que o programa converterá para outras medidas!")
print("-------------------------------------------------------------------------------")

metros=float(input("Digite uma distância em metros: "))

print("-------------------------------------------------------------------------------")

print("A distância em outras medidas é:\n")

mm=metros*1000
cm=metros*100
dm=metros*10
dam=metros/10
hm=metros/100
km=metros/1000

print("", mm, "milímetro(s)")
print("", cm, "centímetro(s)")
print("", dm, "decímetro(s)")
print("", dam, "decâmetro(s)")
print("", hm, "hectômetro(s)")
print("", km, "Quilômetro(s)")

print("-------------------------------------------------------------------------------")