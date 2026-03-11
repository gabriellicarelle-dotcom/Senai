soma = 0
acima_15 = 0
acima_20 = 0
acima_200 = 0
sobrecarga = False
alerta_pressao = False

for i in range(8):
    corrente = float(input(f"Digite a {i + 1} medição de corente (A): "))
    soma += corrente
    
    if  corrente > 15:
        acima_15 += 1
    if corrente > 20:
        sobrecarga = True
        acima_20 += 1
    if corrente > 200:
        alerta_pressao = True
        acima_200 += 1

media = soma / 8

print (f"Medições acima de 15A: {acima_15} ")
print (f"Média da corrente: {media} ")

if sobrecarga:
    print (f"Houve uma sobrecarga no motor {acima_20} vezes") 

if  alerta_pressao:
    print (f"Medição ultrapassou 200A {acima_200} vezes")

    
      

  
        

