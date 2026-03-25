pressao = float(input("Digite a pressão: "))
temperatura = float(input("Digite a temperatura: "))
ciclos = int(input("Digite a quantidade de ciclos: "))

if ciclos < 200:
    desconto = 0
    operacao = "Leve"
elif ciclos < 1000:
    desconto = 0.05
    operacao = "Moderada"
elif ciclos < 2000:
    desconto = 0.10
    operacao = "Intensiva"
else:
    desconto = 0.15
    operacao = "Crítica"


pressao_ajustada = pressao * (1 - desconto)


fator_risco = pressao_ajustada * temperatura


print("\n--- RESULTADO ---")
print(f"Tipo de operação: {operacao}")
print(f"Pressão ajustada: {pressao_ajustada:.2f}")
print(f"Fator de risco: {fator_risco:.2f}")