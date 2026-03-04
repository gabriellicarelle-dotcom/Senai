
maior = float()
menor = float()
soma = 0
acima_cem = 0

for cont in range (10):
    temp = float(input(f"Digite a {cont + 1}ª temperatura: "))
    soma += temp
    if cont == 0:
        maior = temp
        menor = temp

    if temp > maior:
         maior = temp
    if temp < menor:
        menor = temp
    if temp > 100:
        acima_cem += 1
        
media = soma/cont

print(f"Maior temperatura: {maior}°C")
print(f"Menorg temperatura: {menor}°C")
print(f"Vezes que ultrapassou 100°C: {acima_cem} vezes")
print(f"Média das temperaturas: {media}°C")

