print("Bem-vindo ao sistema de qualidade!")
print("Aluno: Gabrielli \n")

soma_calibrada = 0


for i in range(1, 6):
    print(f"\nSensor {i}")
    
    leitura = float(input("Digite a leitura do sensor: "))
    horas = int(input("Digite as horas de uso: "))
    
    if horas < 200:
        ajuste = 0
    elif horas < 1000:
        ajuste = 0.05
    elif horas < 2000:
        ajuste = 0.10
    else:
        ajuste = 0.15
    
    
    leitura_calibrada = leitura * (1 - ajuste)
    
  
    soma_calibrada += leitura_calibrada
    
    print(f"Leitura bruta: {leitura:.2f}")
    print(f"Leitura calibrada: {leitura_calibrada:.2f}")

media = soma_calibrada / 5

print("\n--- RESULTADO FINAL ---")
print(f"Média calibrada dos sensores: {media:.2f}")